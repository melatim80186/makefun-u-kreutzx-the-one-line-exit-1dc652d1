#!/usr/bin/env python3
"""make.fun entry: u-kreutzx-the-one-line-exit-1dc652d1.

Writes the one-line entry to /output/entry.txt.
Python 3, stdlib only, deterministic, no network.
"""

import os

ENTRY = 'I hereby resign from being the only person who knows where anything is — good luck finding the passwords, the files, or me.'


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
