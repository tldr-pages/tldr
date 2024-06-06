#!/usr/bin/env python3
# SPDX-License-Identifier: MIT

"""
A Python script to generate or update alias pages.

Disclaimer: This script generates a lot of false positives so it isn't suggested to use the sync option. If used, only stage changes and commit verified changes for your language by using -l LANGUAGE.

Note: If the current directory or one of its parents is called "tldr", the script will assume it is the tldr root, i.e., the directory that contains a clone of https://github.com/tldr-pages/tldr
If you aren't, the script will use TLDR_ROOT as the tldr root. Also, ensure 'git' is available.

Usage:
    python3 scripts/set-alias-page.py [-p PAGE] [-S] [-l LANGUAGE] [-s] [-n] [COMMAND]

Options:
    -p, --page PAGE
        Specify the alias page in the format "platform/alias_command.md".
    -S, --sync
        Synchronize each translation's alias page (if exists) with that of the English page.
    -l, --language LANGUAGE
        Specify the language, a POSIX Locale Name in the form of "ll" or "ll_CC" (e.g. "fr" or "pt_BR").
    -s, --stage
        Stage modified pages (requires 'git' on $PATH and TLDR_ROOT to be a Git repository).
    -n, --dry-run
        Show what changes would be made without actually modifying the page.

Positional Argument:
    COMMAND          The command to be set as the alias command.

Examples:
    1. Add 'vi' as an alias page of 'vim':
       python3 scripts/set-alias-page.py -p common/vi vim
       python3 scripts/set-alias-page.py --page common/vi vim

    2. Read English alias pages and synchronize them into all translations:
       python3 scripts/set-alias-page.py -S
       python3 scripts/set-alias-page.py --sync

    3. Read English alias pages and synchronize them for Brazilian Portuguese pages only:
       python3 scripts/set-alias-page.py -S -l pt_BR
       python3 scripts/set-alias-page.py --sync --language pt_BR

    4. Read English alias pages, synchronize them into all translations and stage modified pages for commit:
       python3 scripts/set-alias-page.py -Ss
       python3 scripts/set-alias-page.py --sync --stage

    5. Read English alias pages and show what changes would be made:
       python3 scripts/set-alias-page.py -Sn
       python3 scripts/set-alias-page.py --sync --dry-run
"""

import re
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

IGNORE_FILES += ("tldr.md", "aria2.md")


def test_ignore_files():
    assert IGNORE_FILES == (
        ".DS_Store",
        "tldr.md",
        "aria2.md",
    )
    assert ".DS_Store" in IGNORE_FILES
    assert "tldr.md" in IGNORE_FILES


def get_templates(root: Path):
    """
    Get all alias page translation templates from
    TLDR_ROOT/contributing-guides/translation-templates/alias-pages.md.

    Parameters:
    root (Path): The path of local tldr repository, i.e., TLDR_ROOT.

    Returns:
    dict of (str, str): Language labels map to alias page templates.
    """

    template_file = root / "contributing-guides/translation-templates/alias-pages.md"
    with template_file.open(encoding="utf-8") as f:
        lines = f.readlines()

    # Parse alias-pages.md
    templates = {}
    i = 0
    while i < len(lines):
        if lines[i].startswith("###"):
            lang = lines[i][4:].strip("\n").strip(" ")
            while True:
                i = i + 1
                if lines[i].startswith("Not translated yet."):
                    is_translated = False
                    break
                elif lines[i].startswith("```markdown"):
                    i = i + 1
                    is_translated = True
                    break

            if is_translated:
                text = ""
                while not lines[i].startswith("```"):
                    text += lines[i]
                    i = i + 1
                templates[lang] = text

        i = i + 1

    return templates


def set_alias_page(
    path: Path, command: str, dry_run: bool = False, language_to_update: str = ""
) -> str:
    """
    Write an alias page to disk.

    Parameters:
    path (string): Path to an alias page
    command (string): The command that the alias stands for.
    dry_run (bool): Whether to perform a dry-run, i.e. only show the changes that would be made.
    language_to_update (string): Optionally, the language of the translation to be updated.

    Returns:
    str: Execution status
         "" if the alias page standing for the same command already exists or if the locale does not match language_to_update.
         "\x1b[36mpage added"
         "\x1b[34mpage updated"
         "\x1b[36mpage would be added"
         "\x1b[34mpage would updated"
    """

    locale = get_locale(path)
    if locale not in templates or (
        language_to_update != "" and locale != language_to_update
    ):
        # return empty status to indicate that no changes were made
        return ""

    # Test if the alias page already exists
    original_command = get_alias_page(path)
    if original_command == command:
        return ""

    status = get_status(
        "added" if original_command == "" else "updated", dry_run, "page"
    )

    if not dry_run:  # Only write to the path during a non-dry-run
        alias_name = path.stem
        text = (
            templates[locale]
            .replace("example", alias_name, 1)
            .replace("example", command)
        )
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as f:
            f.write(text)

    return status


def get_alias_page(path: Path) -> str:
    """
    Determine whether the given path is an alias page.

    Parameters:
    path (Path): Path to a page

    Returns:
    str: "" If the path doesn't exit or is not an alias page,
         otherwise return what command the alias stands for.
    """

    if not path.exists():
        return ""
    with path.open(encoding="utf-8") as f:
        for line in f:
            # match alias (`tldr <alias>`)
            if match := re.search(r"^`tldr (.+)`", line):
                return match[1]
    return ""


def sync(
    root: Path,
    pages_dirs: list[Path],
    alias_name: str,
    original_command: str,
    dry_run: bool = False,
    language_to_update: str = "",
) -> list[Path]:
    """
    Synchronize an alias page into all translations.

    Parameters:
    root (Path): TLDR_ROOT
    pages_dirs (list of Path's): Path's of page entry and platform, e.g. "page.fr/common".
    alias_name (str): An alias command with .md extension like "vi.md".
    original_command (str): An Original command like "vim".
    dry_run (bool): Whether to perform a dry-run, i.e. only show the changes that would be made.
    language_to_update (str): Optionally, the language of the translation to be updated.

    Returns:
    list (list of Path's): A list of Path's to be staged into git, using by --stage option.
    """
    paths = []
    for page_dir in pages_dirs:
        path = root / page_dir / alias_name
        status = set_alias_page(path, original_command, dry_run, language_to_update)
        if status != "":
            rel_path = "/".join(path.parts[-3:])
            paths.append(rel_path)
            print(create_colored_line(Colors.GREEN, f"{rel_path} {status}"))
    return paths


def main():
    parser = create_argument_parser(
        "Sets the alias page for all translations of a page"
    )
    parser.add_argument("command", type=str, nargs="?", default="")
    args = parser.parse_args()

    root = get_tldr_root()

    # A dictionary of all alias page translations
    global templates
    templates = get_templates(root)
    pages_dirs = get_pages_dir(root)

    target_paths = []

    # Use '--page' option
    if args.page != "":
        target_paths += get_target_paths(args.page, pages_dirs)

        for path in target_paths:
            rel_path = "/".join(path.parts[-3:])
            status = set_alias_page(path, args.command, args.dry_run, args.language)
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
                original_command = get_alias_page(root / "pages" / command)
                if original_command != "":
                    target_paths += sync(
                        root,
                        pages_dirs,
                        command,
                        original_command,
                        args.dry_run,
                        args.language,
                    )

    # Use '--stage' option
    if args.stage and not args.dry_run and len(target_paths) > 0:
        stage(target_paths)


if __name__ == "__main__":
    main()
