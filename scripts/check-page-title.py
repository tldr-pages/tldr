#!/usr/bin/env python3
# SPDX-License-Identifier: MIT

"""
A Python script to check if all page titles match with their filename.

Usage:
    python3 scripts/check-page-title.py [-p PAGE] [-l LANGUAGE]

Options:
    -p, --page PAGE
        Specify the page in the format "platform/command". This option allows checking the title for a specific page.
    -l, --language LANGUAGE
        Specify the language, a POSIX Locale Name in the form of "ll" or "ll_CC" (e.g. "fr" or "pt_BR").

Examples:
    1. Check the page title for a specific page:
       python3 scripts/check-page-title.py -p common/tar
       python3 scripts/check-page-title.py --page common/tar

    2. Check the page titles for Brazilian Portuguese pages only:
       python3 scripts/check-page-title.py -l pt_BR
       python3 scripts/check-page-title.py --language pt_BR
"""

from pathlib import Path
import re
import argparse
from _common import (
    IGNORE_FILES,
    Colors,
    get_tldr_root,
    get_pages_dir,
    get_target_paths,
    get_page_title,
    create_colored_line,
)

IGNORE_LIST = [
    "exclamation mark",
    "caret",
    "dollar sign",
    "tilde",
    "percent sign",
    "curly brace",
    "history expansion",
    "acme.sh   dns",
    "pacman  d",
    "pacman   database",
    "pacman   deptest",
    "pacman  f",
    "pacman   files",
    "pacman  q",
    "pacman   query",
    "pacman  r",
    "pacman   remove",
    "pacman  s",
    "pacman   sync",
    "pacman  t",
    "pacman  u",
    "pacman   upgrade",
    "qm move disk",
    "rename",
    "umount",
]


def normalize_command_name(name: str) -> str:
    name = name.lower()
    name = re.sub(r"nix3", "nix", name)
    name = re.sub(r"\.fish|\.js|\.1", "", name)
    name = name.replace("-", " ")
    return name.strip()


def check_page_title(path: Path) -> str:
    """
    Check if the title of a page matches the filename.
    """
    command_name_file = normalize_command_name(path.stem)
    command_name_page = normalize_command_name(get_page_title(path))

    if command_name_file != command_name_page and command_name_page not in IGNORE_LIST:
        return f"Inconsistency found in file: {path}: {command_name_page} should be {command_name_file}"

    return ""


def main():
    parser = argparse.ArgumentParser(
        description="Check if all page titles match with their filename."
    )
    parser.add_argument(
        "-p",
        "--page",
        type=str,
        default="",
        help='page name in the format "platform/alias_command.md"',
    )
    parser.add_argument(
        "-l",
        "--language",
        type=str,
        default="",
        help='language in the format "ll" or "ll_CC" (e.g. "fr" or "pt_BR")',
    )

    args = parser.parse_args()

    root = get_tldr_root()
    pages_dirs = get_pages_dir(root)

    # Use '--page' option
    if args.page != "":
        target_paths = get_target_paths(args.page, pages_dirs, args.language)

        for path in target_paths:
            rel_path = "/".join(path.parts[-3:])
            status = check_page_title(path)
            if status != "":
                print(create_colored_line(Colors.RED, f"{rel_path} {status}"))
        return

    # Use '--language' option
    if not args.language:
        # Get all language folders (pages.*)
        language_dirs = [d for d in root.iterdir() if d.name.startswith("pages.")]
        locales = [d.name.split(".")[1] for d in language_dirs]
    else:
        locales = [args.language]

    for locale in locales:
        en_path = root / "pages"
        platforms = [i.name for i in en_path.iterdir() if i.name not in IGNORE_FILES]

        for platform in platforms:
            platform_path = en_path / platform
            commands = [
                f"{platform}/{page.name}"
                for page in platform_path.iterdir()
                if page.name not in IGNORE_FILES
            ]

            for command in commands:
                path = root / (f"pages.{locale}") / command
                if path.exists():
                    status = check_page_title(path)
                    if status:
                        rel_path = "/".join(path.parts[-3:])
                        print(create_colored_line(Colors.RED, f"{rel_path} {status}"))


if __name__ == "__main__":
    main()
