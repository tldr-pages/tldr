#!/usr/bin/env python3
# SPDX-License-Identifier: MIT

"""
A Python script to add or update the "See also" section for all translations of a page.

Note: If the current directory or one of its parents is called "tldr", the script will assume it is the tldr root, i.e., the directory that contains a clone of https://github.com/tldr-pages/tldr
If the script doesn't find it in the current path, the environment variable TLDR_ROOT will be used as the tldr root. Also, ensure 'git' is available.

Usage:
    python3 scripts/set-see-also.py [-p PAGE] [-S] [-l LANGUAGE] [-s] [-n] [COMMANDS...]

Options:
    -p, --page PAGE
        Specify the page in the format "platform/command". This option allows setting the link for a specific page.
    -S, --sync
        Synchronize each translation's "See also" section (if exists) with that of the English page.
    -l, --language LANGUAGE
        Specify the language, a POSIX Locale Name in the form of "ll" or "ll_CC" (e.g. "fr" or "pt_BR").
    -s, --stage
        Stage modified pages (requires 'git' on $PATH and TLDR_ROOT to be a Git repository).
    -n, --dry-run
        Show what changes would be made without actually modifying the page.

Positional Argument:
    COMMANDS          The commands to be set in the "See also" section.

Examples:
    1. Set the commands for a specific page:
       python3 scripts/set-see-also.py -p common/tar tar,gtar
       python3 scripts/set-see-also.py --page common/tar tar,gtar

    2. Read English pages and synchronize the "See also" section across translations:
       python3 scripts/set-see-also.py -S
       python3 scripts/set-see-also.py --sync

    3. Read English pages and synchronize the "See also" section for Brazilian Portuguese pages only:
       python3 scripts/set-see-also.py -S -l pt_BR
       python3 scripts/set-see-also.py --sync --language pt_BR

    4. Read English pages, synchronize the "See also" section across translations and stage modified pages for commit:
       python3 scripts/set-see-also.py -Ss
       python3 scripts/set-see-also.py --sync --stage

    5. Show what changes would be made across translations:
       python3 scripts/set-see-also.py -Sn
       python3 scripts/set-see-also.py --sync --dry-run
"""

import re
import sys
from pathlib import Path
from dataclasses import dataclass
from _common import (
    IGNORE_FILES,
    Colors,
    get_tldr_root,
    get_templates,
    get_pages_dirs,
    get_target_paths,
    get_locale,
    get_status,
    stage,
    create_colored_line,
    create_argument_parser,
)


@dataclass
class Config:
    """Global configuration for the script"""

    root: Path
    pages_dirs: list[Path]
    templates: dict[str, str]
    dry_run: bool = False
    language: str = ""


def set_see_also(
    path: Path, see_also: str, dry_run: bool = False, language_to_update: str = ""
) -> str:
    """
    Write a "See also" section in a page to disk.

    Parameters:
    path (string): Path to a page
    see_also (string): The "See also" section to insert.
    dry_run (bool): Whether to perform a dry-run, i.e. only show the changes that would be made.
    language_to_update (string): Optionally, the language of the translation to be updated.

    Returns:
    str: Execution status
         "" if the page does not need an update or if the locale does not match language_to_update.
         "\x1b[36msee also added"
         "\x1b[34msee also updated"
         "\x1b[36msee also would be added"
         "\x1b[34msee also would be updated"
    """

    locale = get_locale(path)
    if locale not in config.templates or (
        language_to_update != "" and locale != language_to_update
    ):
        # return empty status to indicate that no changes were made
        return ""

    with path.open(encoding="utf-8") as f:
        lines = f.readlines()

    desc_start = 0
    desc_end = 0

    # find start and end of description
    for i, line in enumerate(lines):
        if line.startswith(">") and desc_start == 0:
            desc_start = i
        if not lines[i + 1].startswith(">") and desc_start != 0:
            desc_end = i
            break

    new_line = config.templates[locale].replace("`example`", see_also)

    if lines[desc_end - 1] == new_line:
        # return empty status to indicate that no changes were made
        return ""

    if re.search(r"^>.*: `", lines[desc_end - 1]):
        # overwrite second last line
        lines[desc_end - 1] = new_line
        action = "updated"
    else:
        # add new line
        lines.insert(desc_end, new_line)
        action = "added"

    status = get_status(action, dry_run, "see also")

    if not dry_run:  # Only write to the path during a non-dry-run
        with path.open("w", encoding="utf-8") as f:
            f.writelines(lines)

    return status


def get_see_also(path: Path) -> str:
    """
    Determine whether the given path has a "See also" section.

    Parameters:
    path (Path): Path to a page

    Returns:
    str: "" If the path doesn't exit or does not have a link,
         otherwise return the "See also" section.
    """

    if not path.exists():
        return ""
    with path.open(encoding="utf-8") as f:
        lines = f.readlines()

    desc_start = 0
    desc_end = 0

    # find start and end of description
    for i, line in enumerate(lines):
        if line.startswith(">") and desc_start == 0:
            desc_start = i
        if not lines[i + 1].startswith(">") and desc_start != 0:
            desc_end = i
            break

    candidate = lines[desc_end - 1]

    if not re.match(r"^> See also:", candidate):
        return ""

    commands = re.findall(r"`([^`]+)`", candidate)
    if not commands:
        return ""

    # Normalise spacing and output format used by your template
    return ", ".join(f"`{command.strip()}`" for command in commands)


def sync(
    root: Path,
    pages_dirs: list[Path],
    command: str,
    see_also: str,
    dry_run: bool = False,
    language_to_update: str = "",
) -> list[Path]:
    """
    Synchronize a "See also" section into all translations.

    Parameters:
    root (Path): TLDR_ROOT
    pages_dirs (list of Path's): Path's of page entry and platform, e.g. "page.fr/common".
    command (str): A command like "tar".
    see_also (str): A "See also" section like "gtar".
    dry_run (bool): Whether to perform a dry-run, i.e. only show the changes that would be made.
    language_to_update (str): Optionally, the language of the translation to be updated.

    Returns:
    list (list of Path's): A list of Path's to be staged into git, using by --stage option.
    """
    paths = []
    for page_dir in pages_dirs:
        path = root / page_dir / command
        if path.exists():
            status = set_see_also(path, see_also, dry_run, language_to_update)
            if status != "":
                rel_path = "/".join(path.parts[-3:])
                paths.append(rel_path)
                print(create_colored_line(Colors.GREEN, f"{rel_path} {status}"))
    return paths


def main():
    parser = create_argument_parser(
        'Sets the "See also" section for all translations of a page'
    )
    parser.add_argument("see_also", type=str, nargs="?", default="")
    args = parser.parse_args()

    # Print usage information if no arguments were provided
    if len(sys.argv) == 1:
        parser.print_help()
        return

    root = get_tldr_root()
    pages_dirs = get_pages_dirs(root)
    templates = get_templates(root, "see-also-mentions.md")

    global config
    config = Config(
        root=root,
        pages_dirs=pages_dirs,
        templates=templates,
        dry_run=args.dry_run,
        language=args.language,
    )

    target_paths = []

    # Use '--page' option
    if args.page != "":
        target_paths += get_target_paths(args.page, pages_dirs)

        for path in target_paths:
            rel_path = "/".join(path.parts[-3:])
            status = set_see_also(path, args.see_also, args.dry_run, args.language)
            if status != "":
                print(create_colored_line(Colors.GREEN, f"{rel_path} {status}"))

    # Use '--sync' option
    elif args.sync:
        pages_dirs.remove(root / "pages")
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
                see_also = get_see_also(root / "pages" / command)
                if see_also != "":
                    target_paths += sync(
                        root, pages_dirs, command, see_also, args.dry_run, args.language
                    )

    # Use '--stage' option
    if args.stage and not args.dry_run and len(target_paths) > 0:
        stage(target_paths)


if __name__ == "__main__":
    main()
