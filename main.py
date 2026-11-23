"""Real-Life Patch Notes: The Comedy Changelog.

Writes one one-line patch note for a bug in real life / human biology
to /output/entry.txt. Deterministic, stdlib only.
"""

import os
import sys

ENTRY = (
    "v2.4.1: fixed a bug where the brain replayed your most embarrassing "
    "moment from 2011 every night at 3 a.m. instead of sleeping."
)

MAX_CHARS = 160
OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> None:
    """Gate: the entry must be a single non-blank line of 1-160 characters."""
    if not line or not line.strip():
        raise ValueError("entry is blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(line)} characters, over the {MAX_CHARS} limit"
        )


def main() -> int:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    print(f"wrote {len(ENTRY)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
