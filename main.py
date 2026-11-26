#!/usr/bin/env python3
"""Painfully Honest Out-of-Office entry.

Writes a single honest-but-polite out-of-office auto-reply to
/output/entry.txt, with no trailing newline. Stdlib only, deterministic.
"""

import os


ENTRY = (
    "I'm away this week and, honestly, relieved to step back "
    "from an inbox that had quietly become a second job, "
    "so thank you for your patience while I catch up slowly."
)


def main() -> None:
    # One sentence, 163 characters, well inside the 200-character gate.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip() == ENTRY, "entry must not have outer whitespace"
    assert ENTRY.count(".") == 1 and ENTRY.endswith("."), "one sentence only"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

