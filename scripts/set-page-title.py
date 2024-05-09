#!/usr/bin/env python3
# SPDX-License-Identifier: MIT

"""
This script sets the title for all translations of a page.
It can be used to update the titles in translations.

Note: If the current directory or one of its parents is called "tldr", the script will assume it is the tldr root, i.e., the directory that contains a clone of https://github.com/tldr-pages/tldr
If you aren't, the script will use TLDR_ROOT as the tldr root. Also, ensure 'git' is available.

Usage: python3 scripts/set-page-title.py [-p PAGE] [-s] [-S] [-n] [TITLE]

Supported Arguments:
    -p, --page    Specify the page name in the format "platform/command.md".
                  This option allows setting the title for a specific page.
    -s, --stage   Stage modified pages for commit. This option requires 'git'
                  to be on the $PATH and TLDR_ROOT to be a Git repository.
    -S, --sync    Synchronize each translation's title (if
                  exists) with that of the English page. This is useful to
                  ensure consistency across translations.
    -n, --dry-run Show what changes would be made without actually modifying the page.

Positional Argument:
    TITLE          The title to be set as the title.

Examples:
    1. Set the title for a specific page:
       python3 scripts/set-page-title.py -p common/tar.md tar.1

    2. Synchronize titles across translations:
       python3 scripts/set-page-title.py -S

    3. Synchronize titles across translations and stage modified pages for commit:
       python3 scripts/set-page-title.py -Ss
       python3 scripts/set-page-title.py --sync --stage

    4. Show what changes would be made across translations:
       python3 scripts/set-page-title.py -Sn
       python3 scripts/set-page-title.py --sync --dry-run
"""

import argparse
import os
import subprocess
from pathlib import Path

IGNORE_FILES = (".DS_Store",)


def get_tldr_root() -> Path:
    # If this script is running from tldr/scripts, the parent's parent is the root
    f = Path(__file__).resolve()
    if (
        tldr_root := next((path for path in f.parents if path.name == "tldr"), None)
    ) is not None:
        return tldr_root
    elif "TLDR_ROOT" in os.environ:
        return Path(os.environ["TLDR_ROOT"])
    raise SystemExit(
        "\x1b[31mPlease set TLDR_ROOT to the location of a clone of https://github.com/tldr-pages/tldr."
    )


def set_title(path: Path, title: str, dry_run=False) -> str:
    new_line = f"# {title}\n"

    # Read the content of the Markdown file
    with path.open(encoding="utf-8") as f:
        lines = f.readlines()

    if lines[0] == new_line:
        # return empty status to indicate that no changes were made
        return ""

    if dry_run:
        status = "title would be updated"
    else:
        status = "title updated"

    status = f"\x1b[34m{status}\x1b[0m"

    if not dry_run:
        lines[0] = new_line
        with path.open("w", encoding="utf-8") as f:
            f.writelines(lines)

    return status


def get_title(path: Path) -> str:
    with path.open(encoding="utf-8") as f:
        first_line = f.readline().strip()

    return first_line.split("#", 1)[-1].strip()


def sync(
    root: Path, pages_dirs: list[str], command: str, title: str, dry_run=False
) -> list[str]:
    paths = []
    for page_dir in pages_dirs:
        path = root / page_dir / command
        if path.exists():
            rel_path = "/".join(path.parts[-3:])
            status = set_title(path, title, dry_run)
            if status != "":
                paths.append(path)
                print(f"\x1b[32m{rel_path} {status}\x1b[0m")
    return paths


def main():
    parser = argparse.ArgumentParser(
        description="Sets the title for all translations of a page"
    )
    parser.add_argument(
        "-p",
        "--page",
        type=str,
        required=False,
        default="",
        help='page name in the format "platform/command.md"',
    )
    parser.add_argument(
        "-s",
        "--stage",
        action="store_true",
        default=False,
        help="stage modified pages (requires `git` to be on $PATH and TLDR_ROOT to be a Git repository)",
    )
    parser.add_argument(
        "-S",
        "--sync",
        action="store_true",
        default=False,
        help="synchronize each translation's title (if exists) with that of English page",
    )
    parser.add_argument(
        "-n",
        "--dry-run",
        action="store_true",
        default=False,
        help="show what changes would be made without actually modifying the pages",
    )
    parser.add_argument("title", type=str, nargs="?", default="")
    args = parser.parse_args()

    root = get_tldr_root()
    pages_dirs = [d for d in root.iterdir() if d.name.startswith("pages")]

    target_paths = []

    # Use '--page' option
    if args.page != "":
        if not args.page.lower().endswith(".md"):
            args.page = f"{args.page}.md"
        arg_platform, arg_page = args.page.split("/")

        for pages_dir in pages_dirs:
            page_path = pages_dir / arg_platform / arg_page
            if not page_path.exists():
                continue
            target_paths.append(page_path)

        target_paths.sort()

        for path in target_paths:
            rel_path = "/".join(path.parts[-3:])
            status = set_title(path, args.title)
            if status != "":
                print(f"\x1b[32m{rel_path} {status}\x1b[0m")

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
                if page not in IGNORE_FILES
            ]
            for command in commands:
                title = get_title(root / "pages" / command)
                if title != "":
                    target_paths += sync(root, pages_dirs, command, title, args.dry_run)

    if args.stage and not args.dry_run and len(target_paths) > 0:
        subprocess.call(["git", "add", *target_paths], cwd=root)


if __name__ == "__main__":
    main()
