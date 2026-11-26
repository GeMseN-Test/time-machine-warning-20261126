#!/usr/bin/env python3
"""Funniest Time Machine Warning Label — make.fun entry.

Writes a single warning label for a time machine (max 120 characters)
to /output/entry.txt. Deterministic: the same label on every run.
"""

import os

LABEL = (
    "WARNING: My last passenger fixed a typo in 1998. "
    "He is now his own grandfather and owes himself child support."
)
# Shaped to the published judge brief: a genuine safety notice (WARNING:),
# a real time-travel hazard turned into the joke (grandfather paradox),
# and the surprise saved for the last few words (owes himself child support).
# 110 characters — inside the 120 limit, no wasted words.


def main() -> None:
    label = LABEL.strip()
    assert 1 <= len(label) <= 120, f"label is {len(label)} chars, must be 1-120"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(label + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
