#!/usr/bin/env python3
"""Append one validated entry to AY cognition store."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import sys
from pathlib import Path


VALID_TYPES = [
    "principle",
    "taste",
    "strategy",
    "collaboration",
    "resource",
]

VALID_CONFIDENCE = [
    "high",
    "medium",
    "low",
]


def strip_code_blocks(text: str) -> str:
    return re.sub(r"```.*?```", "", text, flags=re.DOTALL)


def next_cog_id(text: str) -> str:
    body = strip_code_blocks(text)
    ids = [int(match) for match in re.findall(r"^## COG-(\d{3,}):", body, re.MULTILINE)]
    return f"COG-{(max(ids) + 1) if ids else 1:03d}"


def table_value(value: str) -> str:
    value = re.sub(r"\s+", " ", value.strip())
    return value.replace("|", r"\|")


def non_empty(value: str) -> str:
    value = value.strip()
    if not value:
        raise argparse.ArgumentTypeError("value must not be empty")
    return value


def valid_date(value: str) -> str:
    try:
        return dt.date.fromisoformat(value).isoformat()
    except ValueError as exc:
        raise argparse.ArgumentTypeError("expected a real date in YYYY-MM-DD format") from exc


def is_deployed_skill_path(path: Path) -> bool:
    codex_home = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex")).expanduser().resolve()
    try:
        path.resolve().relative_to((codex_home / "skills").resolve())
    except ValueError:
        return False
    return True


def build_entry(args: argparse.Namespace, entry_id: str) -> str:
    title = table_value(args.title)
    fields = {
        "Type": args.type,
        "Trigger": table_value(args.trigger),
        "Decision effect": table_value(args.decision_effect),
        "Evidence": table_value(args.evidence),
        "Confidence": args.confidence,
        "Updated": args.updated,
    }
    lines = [
        f"## {entry_id}: {title}",
        "",
        "| Field | Value |",
        "| --- | --- |",
    ]
    lines.extend(f"| {key} | {value} |" for key, value in fields.items())
    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Append one structured cognition entry to ay.skill."
    )
    parser.add_argument(
        "--file",
        required=True,
        help="canonical workspace cognition store; deployed CODEX_HOME skills are read-only",
    )
    parser.add_argument("--title", required=True, type=non_empty, help="short cognition title")
    parser.add_argument("--type", required=True, choices=VALID_TYPES)
    parser.add_argument(
        "--decision-effect",
        required=True,
        type=non_empty,
        help="what should change in Codex's decision or output",
    )
    parser.add_argument("--trigger", required=True, type=non_empty, help="when this cognition should apply")
    parser.add_argument(
        "--evidence",
        required=True,
        type=non_empty,
        help="where this cognition came from",
    )
    parser.add_argument("--confidence", required=True, choices=VALID_CONFIDENCE)
    parser.add_argument(
        "--updated",
        default=dt.date.today().isoformat(),
        type=valid_date,
        help="entry date in YYYY-MM-DD format",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="print the generated entry without writing the file",
    )
    parser.add_argument(
        "--expect-file-sha",
        help="required for writes; must match the SHA printed by the reviewed dry-run",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    path = Path(args.file).expanduser().resolve()
    if not path.exists():
        print(f"missing cognition store: {path}", file=sys.stderr)
        return 2

    if not args.dry_run and is_deployed_skill_path(path):
        print(
            "refusing to write a deployed CODEX_HOME skill; update the canonical workspace source",
            file=sys.stderr,
        )
        return 2

    text = path.read_text(encoding="utf-8")
    current_sha = hashlib.sha256(text.encode("utf-8")).hexdigest()
    if not args.dry_run:
        if not args.expect_file_sha:
            print(
                f"refusing to write without --expect-file-sha {current_sha}",
                file=sys.stderr,
            )
            return 2
        if args.expect_file_sha != current_sha:
            print("refusing to write: cognition store changed after review", file=sys.stderr)
            return 1
    entry_id = next_cog_id(text)
    entry = build_entry(args, entry_id)

    result = {
        "file": str(path),
        "id": entry_id,
        "dry_run": args.dry_run,
        "current_file_sha256": current_sha,
    }

    if args.dry_run:
        result["entry"] = entry.rstrip()
    else:
        updated_text = text.rstrip() + "\n\n" + entry
        temp_path = path.with_name(f".{path.name}.tmp-{os.getpid()}")
        try:
            temp_path.write_text(updated_text, encoding="utf-8")
            os.replace(temp_path, path)
        finally:
            if temp_path.exists():
                temp_path.unlink()
        result["updated_file_sha256"] = hashlib.sha256(
            updated_text.encode("utf-8")
        ).hexdigest()

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
