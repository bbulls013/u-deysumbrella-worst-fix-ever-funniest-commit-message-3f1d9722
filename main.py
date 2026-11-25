#!/usr/bin/env python3
"""Worst Fix Ever: the funniest commit message for the worst fix ever.

Writes one fixed commit message to /output/entry.txt. The text is a constant,
so every run produces byte-identical output.
"""
import os
from pathlib import Path

LINE = (
    "fix: removed the bug by deleting the feature, the tests, and my will to "
    "investigate. Ship it."
)


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")
    print(f"wrote {out} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
