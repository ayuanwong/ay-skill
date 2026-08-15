#!/usr/bin/env python3
"""Query AY cognition-store entries by keyword."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


DEFAULT_STORE = Path(__file__).resolve().parents[1] / "references" / "cognition-store.md"
FIELDS = [
    "Type",
    "Trigger",
    "Decision effect",
    "Evidence",
    "Confidence",
    "Updated",
]


def strip_code_blocks(text: str) -> str:
    return re.sub(r"```.*?```", "", text, flags=re.DOTALL)


def parse_table(body: str) -> dict[str, str]:
    data: dict[str, str] = {}
    for line in body.splitlines():
        match = re.match(r"^\| ([^|]+) \| (.*) \|$", line)
        if not match:
            continue
        key = match.group(1).strip()
        value = match.group(2).strip()
        if key in FIELDS:
            data[key] = value.replace(r"\|", "|")
    return data


def parse_entries(text: str) -> list[dict[str, str]]:
    text = strip_code_blocks(text)
    pattern = re.compile(r"^## (COG-\d{3,}): (.+)$", re.MULTILINE)
    matches = list(pattern.finditer(text))
    entries: list[dict[str, str]] = []
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        fields = parse_table(text[start:end])
        entries.append(
            {
                "id": match.group(1),
                "title": match.group(2).strip(),
                "type": fields.get("Type", ""),
                "trigger": fields.get("Trigger", ""),
                "decision_effect": fields.get("Decision effect", ""),
                "evidence": fields.get("Evidence", ""),
                "confidence": fields.get("Confidence", ""),
                "updated": fields.get("Updated", ""),
            }
        )
    return entries


def match_score(entry: dict[str, str], terms: list[str]) -> int:
    haystack = " ".join(entry.values()).lower()
    return sum(1 for term in terms if term in haystack)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Find decision-relevant entries in AY cognition store."
    )
    parser.add_argument("query", nargs="*", help="keywords to search")
    parser.add_argument("--file", default=str(DEFAULT_STORE), help="cognition store path")
    parser.add_argument("--type", choices=["principle", "taste", "strategy", "collaboration", "resource"])
    parser.add_argument("--limit", type=int, default=8)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    path = Path(args.file).expanduser()
    entries = parse_entries(path.read_text(encoding="utf-8"))

    terms = [term.lower() for term in args.query if term.strip()]
    rows = []
    for entry in entries:
        if args.type and entry.get("type") != args.type:
            continue
        score = match_score(entry, terms) if terms else 1
        if score <= 0:
            continue
        row = dict(entry)
        row["score"] = score
        rows.append(row)

    rows.sort(key=lambda item: (-int(item["score"]), item["id"]))
    if args.limit > 0:
        rows = rows[: args.limit]

    print(json.dumps({"file": str(path), "query": args.query, "matches": rows}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
