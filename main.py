#!/usr/bin/env python3
"""Say What Actually Broke.

Writes exactly one line of error copy (at most 200 characters) to
/output/entry.txt. Deterministic: the same bytes on every run.
"""

import os

ENTRY = (
    "Upload failed: the server ran out of disk space, and the disk is "
    "full of logs explaining why the server ran out of disk space."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
