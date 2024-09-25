#!/usr/bin/env python3
# SPDX-License-Identifier: MIT

"""
A Python script to add or update the page title for all translations of a page.

Note: If the current directory or one of its parents is called "tldr", the script will assume it is the tldr root, i.e., the directory that contains a clone of https://github.com/tldr-pages/tldr
If the script doesn't find it in the current path, the environment variable TLDR_ROOT will be used as the tldr root. Also, ensure 'git' is available.

Usage:
    python3 scripts/set-page-title.py [-p PAGE] [-S] [-l LANGUAGE] [-s] [-n] [TITLE]

Options:
    -p, --page PAGE
        Specify the page in the format "platform/command". This option allows setting the title for a specific page.
    -S, --sync
        Synchronize each translation's title (if exists) with that of the English page.
    -l, --language LANGUAGE
        Specify the language, a POSIX Locale Name in the form of "ll" or "ll_CC" (e.g. "fr" or "pt_BR").
    -s, --stage
        Stage modified pages (requires 'git' on $PATH and TLDR_ROOT to be a Git repository).
    -n, --dry-run
        Show what changes would be made without actually modifying the page.

Positional Argument:
    TITLE          The title to be set as the title.

Examples:
    1. Set the title for a specific page:
       python3 scripts/set-page-title.py -p common/tar tar
       python3 scripts/set-page-title.py --page common/tar tar

    2. Synchronize titles across translations:
       python3 scripts/set-page-title.py -S
       python3 scripts/set-page-title.py --sync

    3. Read English pages and synchronize the title for Brazilian Portuguese pages only:
       python3 scripts/set-page-title.py -S -l pt_BR
       python3 scripts/set-page-title.py --sync --language pt_BR

    4. Synchronize titles across translations and stage modified pages for commit:
       python3 scripts/set-page-title.py -Ss
       python3 scripts/set-page-title.py --sync --stage

    5. Show what changes would be made across translations:
       python3 scripts/set-page-title.py -Sn
       python3 scripts/set-page-title.py --sync --dry-run
"""

from pathlib import Path
from _common import (
    IGNORE_FILES,
    Colors,
    get_tldr_root,
    get_pages_dir,
    get_target_paths,
    get_locale,
    get_status,
    stage,
    create_colored_line,
    create_argument_parser,
)


def set_page_title(
    path: Path, title: str, dry_run: bool = False, language_to_update: str = ""
) -> str:
    """
    Write a title in a page to disk.

    Parameters:
    path (string): Path to a page
    title (string): The title to insert.
    dry_run (bool): Whether to perform a dry-run, i.e. only show the changes that would be made.
    language_to_update (string): Optionally, the language of the translation to be updated.

    Returns:
    str: Execution status
         "" if the page does not need an update or if the locale does not match language_to_update.
         "\x1b[36mtitle added"
         "\x1b[34mtitle updated"
         "\x1b[36mtitle would be added"
         "\x1b[34mtitle would updated"
    """

    locale = get_locale(path)
    if language_to_update != "" and locale != language_to_update:
        # return empty status to indicate that no changes were made
        return ""

    new_line = f"# {title}\n"

    # Read the content of the Markdown file
    with path.open(encoding="utf-8") as f:
        lines = f.readlines()

    if lines[0] == new_line:
        # return empty status to indicate that no changes were made
        return ""

    status = get_status("updated", dry_run, "title")

    if not dry_run:  # Only write to the path during a non-dry-run
        lines[0] = new_line
        with path.open("w", encoding="utf-8") as f:
            f.writelines(lines)

    return status


def get_page_title(path: Path) -> str:
    """
    Determine whether the given path has a title.

    Parameters:
    path (Path): Path to a page

    Returns:
    str: "" If the path doesn't exit or does not have a title,
         otherwise return the page title.
    """

    if not path.exists():
        return ""
    with path.open(encoding="utf-8") as f:
        first_line = f.readline().strip()

    return first_line.split("#", 1)[-1].strip()


def sync(
    root: Path,
    pages_dirs: list[Path],
    command: str,
    title: str,
    dry_run: bool = False,
    language_to_update: str = "",
) -> list[str]:
    """
    Synchronize a page title into all translations.

    Parameters:
    root (Path): TLDR_ROOT
    pages_dirs (list of Path's): Path's of page entry and platform, e.g. "page.fr/common".
    command (str): A command like "tar".
    title (str): A title like "tar".
    dry_run (bool): Whether to perform a dry-run, i.e. only show the changes that would be made.
    language_to_update (str): Optionally, the language of the translation to be updated.

    Returns:
    list (list of Path's): A list of Path's to be staged into git, using by --stage option.
    """
    paths = []
    for page_dir in pages_dirs:
        path = root / page_dir / command
        if path.exists():
            status = set_page_title(path, title, dry_run, language_to_update)
            if status != "":
                rel_path = "/".join(path.parts[-3:])
                paths.append(rel_path)
                print(create_colored_line(Colors.GREEN, f"{rel_path} {status}"))
    return paths


def main():
    parser = create_argument_parser("Sets the title for all translations of a page")
    parser.add_argument("title", type=str, nargs="?", default="")
    args = parser.parse_args()

    root = get_tldr_root()
    pages_dirs = get_pages_dir(root)

    target_paths = []

    # Use '--page' option
    if args.page != "":
        target_paths += get_target_paths(args.page, pages_dirs)

        for path in target_paths:
            rel_path = "/".join(path.parts[-3:])
            status = set_page_title(path, args.title)
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
                title = get_page_title(root / "pages" / command)
                if title != "":
                    target_paths += sync(
                        root, pages_dirs, command, title, args.dry_run, args.language
                    )

    # Use '--stage' option
    if args.stage and not args.dry_run and len(target_paths) > 0:
        stage(target_paths)


if __name__ == "__main__":
    main()
