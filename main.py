"""Writes one short safety warning label for make.fun.

The text below is the whole entry. It is written as UTF-8 bytes, with no
trailing newline, into MAKEFUN_OUTPUT_DIR (default /output).
"""

import os
import sys
from pathlib import Path

TEXT = "WARNING: Says 'no rush' while standing over you with their coat on."

OUTPUT_NAME = "entry.txt"


def out_dir() -> Path:
    """Directory named by MAKEFUN_OUTPUT_DIR, else OUTPUT_DIR, else /output."""
    return Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )


def main() -> int:
    assert 1 <= len(TEXT) <= 280, "entry text must be 1..280 characters"

    target = out_dir()
    target.mkdir(parents=True, exist_ok=True)

    (target / OUTPUT_NAME).write_bytes(TEXT.encode("utf-8"))

    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
