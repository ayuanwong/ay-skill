#!/usr/bin/env python3
"""Audit AY cognition-store entry shape."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
from pathlib import Path


REQUIRED_FIELDS = [
    "Type",
    "Trigger",
    "Decision effect",
    "Evidence",
    "Confidence",
    "Updated",
]
VALID_TYPES = {"principle", "taste", "strategy", "collaboration", "resource"}
VALID_CONFIDENCE = {"high", "medium", "low"}


def parse_entries(text: str) -> list[tuple[str, str]]:
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    pattern = re.compile(r"^## (COG-\d{3,}: .+)$", re.MULTILINE)
    matches = list(pattern.finditer(text))
    entries: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        entries.append((match.group(1), text[start:end]))
    return entries


def field_values(body: str) -> dict[str, str]:
    values: dict[str, str] = {}
    for field in REQUIRED_FIELDS:
        match = re.search(
            rf"^\| {re.escape(field)} \| (.*?) \|$",
            body,
            re.MULTILINE,
        )
        values[field] = match.group(1).strip().replace(r"\|", "|") if match else ""
    return values


def audit(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    entries = parse_entries(text)
    warnings = []
    entry_results = []

    text_without_code = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    header_like = re.findall(
        r"^##\s+(COG-[^:\s]+)(?::.*?)?$", text_without_code, re.MULTILINE
    )
    parsed_ids = [title.split(":", 1)[0] for title, _ in entries]
    malformed_headers = [item for item in header_like if item not in parsed_ids]
    if malformed_headers:
        warnings.append("malformed_cognition_headers:" + ",".join(malformed_headers))

    if not entries:
        warnings.append("no_cognition_entries")

    seen_ids = set()
    numeric_ids = []
    for title, body in entries:
        entry_id = title.split(":", 1)[0]
        numeric_ids.append(int(entry_id.split("-", 1)[1]))
        if entry_id in seen_ids:
            warnings.append(f"duplicate_id:{entry_id}")
        seen_ids.add(entry_id)
        values = field_values(body)
        missing = [field for field, value in values.items() if not value]
        if missing:
            warnings.append(f"missing_fields:{entry_id}:{','.join(missing)}")
        invalid = []
        if values["Type"] and values["Type"] not in VALID_TYPES:
            invalid.append("Type")
        if values["Confidence"] and values["Confidence"] not in VALID_CONFIDENCE:
            invalid.append("Confidence")
        if values["Updated"]:
            try:
                dt.date.fromisoformat(values["Updated"])
            except ValueError:
                invalid.append("Updated")
        if invalid:
            warnings.append(f"invalid_fields:{entry_id}:{','.join(invalid)}")
        entry_results.append(
            {
                "id": entry_id,
                "title": title,
                "missing": missing,
                "invalid": invalid,
            }
        )

    if numeric_ids != sorted(numeric_ids):
        warnings.append("cognition_ids_not_monotonic")

    return {
        "file": str(path),
        "entry_count": len(entries),
        "entries": entry_results,
        "warnings": warnings,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="cognition-store markdown file")
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    result = audit(Path(args.file))
    print(json.dumps(result, ensure_ascii=False, indent=2))

    if args.strict and result["warnings"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
