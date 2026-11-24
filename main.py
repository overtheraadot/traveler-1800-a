#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single sentence (at most 200 characters) explaining the modern
internet to a time traveler who has just stepped out of the year 1800.

The sentence builds only from things a person from 1800 already knows --
letters, books, maps -- and pictures the internet as one glowing pane of
glass holding them all, ready the moment you wish for one.
"""

import os

LINE = (
    "Imagine every letter, book, and map in the world stacked inside one "
    "glowing pane of glass, and any of them arriving in your hands the "
    "moment you wish for it \u2014 that is the internet."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
