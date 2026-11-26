#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence to /output/entry.txt.
"""
import os

LINE = (
    "He can write a 400-page bill to regulate the internet, "
    "but the bill still has to be turned into a PDF by his "
    "twenty-three-year-old intern."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
