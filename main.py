#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — entry program.

Writes exactly one emoji to /output/entry.txt: the desert island
(U+1F3DD). A tiny island with a single palm tree, ringed by blue sea —
the whole dream vacation in one picture. It was picked over the generic
beach or plane because it is specific rather than generic: not just any
holiday, but the fantasy of escaping to a place with nothing to do and
nowhere to be. It reads instantly at small size on any screen, needs no
words, and lands as a postcard at a glance — sun, sea, and solitude in a
single character (4 bytes of UTF-8, no variation selector needed, since
U+1F3DD already has default emoji presentation).
"""

import os

EMOJI = "\U0001F3DD"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if len(EMOJI) != 1 or EMOJI.isspace():
        raise ValueError("entry must be exactly one non-whitespace character")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
