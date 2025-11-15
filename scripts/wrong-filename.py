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
    "jc.json",
    "lid.libuser",
    "mc.cli",
    "mc.fm",
    "pacman d",
    "pacman f",
    "pacman q",
    "pacman r",
    "pacman s",
    "pacman t",
    "pacman u",
    "parted",
    "print.runmailcap",
    "print.win",
    "print.zsh",
    "python m json.tool",
    "rename",
    "snap.esa",
    "snap.pkg",
}


def normalize(text: str) -> str:
    """
    Normalize a string:
    - replace '-' with spaces
    - lowercase
    - collapse multiple spaces into one
    - strip leading/trailing whitespace
    """
    text = text.replace("-", " ").lower().strip()
    text = re.sub(r"\s+", " ", text)
    return text


def check_file(path: Path) -> str | None:
    """Check a single markdown file for name/title consistency."""
    filename = path.name

    # Remove known suffixes
    command_file = filename
    for suffix in (".md", ".fish", ".js", ".1", ".2", ".3"):
        if command_file.endswith(suffix):
            command_file = command_file[: -len(suffix)]
    command_file = normalize(command_file)

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

    if command_file != command_page:
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
