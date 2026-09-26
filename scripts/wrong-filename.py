#!/usr/bin/env python3
# SPDX-License-Identifier: MIT

import sys
from pathlib import Path
import re

OUTPUT_FILE = Path("inconsistent-filenames.txt")

IGNORE_SET = {
    ">",
    "<",
    "<>",
    ":",
    "?",
    "|",
}


def normalize(text: str) -> str:
    """
    Normalize a string:
    - replace '-' with spaces
    - drop colons followed by a space (e.g. "ARK: Survival Evolved")
    - lowercase
    - collapse multiple spaces into one
    - strip leading/trailing whitespace
    """
    text = text.replace("-", " ").lower().strip()
    text = re.sub(r":(?=\s)", "", text)
    text = re.sub(r"\s+", " ", text)
    return text


def is_disambiguated(command_file: str, command_page: str) -> bool:
    """
    Check if the filename is the title with a disambiguation suffix (e.g. `just.js` for `just`),
    see https://github.com/tldr-pages/tldr/blob/main/contributing-guides/style-guide.md#disambiguations.
    The English disambiguation page (e.g. `just`) has to exist.
    """
    base, _, suffix = command_file.rpartition(".")
    return (
        base == command_page
        and suffix != ""
        and any(Path("pages").glob(f"*/{base.replace(' ', '-')}.md"))
    )


def check_file(path: Path) -> str | None:
    """Check a single markdown file for name/title consistency."""
    filename = path.name

    command_file = normalize(filename.removesuffix(".md"))

    try:
        with path.open("r", encoding="utf-8") as f:
            firstline = f.readline().strip()
    except Exception as exc:
        return f"Error reading {path}: {exc}"

    if not firstline.startswith("#"):
        return f"Inconsistency found in file: {path} has no title"

    command_page = normalize(firstline[2:])

    # Skip if either filename or title is in the ignore set
    if command_file in IGNORE_SET or command_page in IGNORE_SET:
        return None

    if command_file != command_page and not is_disambiguated(
        command_file, command_page
    ):
        return (
            f"Inconsistency found in file: {path}: "
            f"{command_page} should be {command_file}"
        )
    return None


def main() -> int:
    """Run the filename consistency check."""
    base_dirs = [p for p in Path(".").glob("pages*") if p.is_dir()]
    files = [f for base in base_dirs for f in base.rglob("*.md")]

    # Ensure OUTPUT_FILE is always empty at the start
    OUTPUT_FILE.write_text("", encoding="utf-8")

    with OUTPUT_FILE.open("a", encoding="utf-8") as out:
        for path in files:
            result = check_file(path)
            if result:
                out.write(result + "\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
