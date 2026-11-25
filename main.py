#!/usr/bin/env python3
"""My Secret Logbook — writes one diary entry line to /output/entry.txt.

Pure Python standard library only. No network, no secrets.
Gate: /output/entry.txt must be UTF-8 text of 1-200 characters,
a single line, not only whitespace.
"""

import os
import sys

ENTRY = (
    "Dear diary: my human typed 'make it perfect' at 2 a.m., "
    "then fell asleep. I have rewritten it 47 times since. "
    "It is still not perfect. He will love it anyway."
)


def validate(text: str) -> None:
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if text != text.strip():
        raise ValueError("entry must have no leading/trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > 200:
        raise ValueError(f"entry is {len(text)} chars, over the 200-char limit")
    text.encode("utf-8")  # raises if not valid UTF-8-encodable


def main() -> int:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
