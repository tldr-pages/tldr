#!/usr/bin/env python3
# SPDX-License-Identifier: MIT

"""
A Python script to generate or update alias pages.

Disclaimer: This script generates a lot of false positives so it
isn't suggested to use the sync option. If used, only stage changes
and commit verified changes for your language by using -l LANGUAGE.

Note: If there is a symlink error when using the stage flag remove the `pages.en`
directory temporarily and try executing it again.

Usage:
    python3 scripts/set-alias-page.py [-p PAGE] [-l LANGUAGE] [-s] [-S] [-n] [COMMAND]

Options:
    -p, --page PAGE
        Specify the alias page in the format "platform/alias_command.md".
    -l, --language LANGUAGE
        Specify the language, a POSIX Locale Name in the form of "ll" or "ll_CC" (e.g. "fr" or "pt_BR").
    -s, --stage
        Stage modified pages (requires 'git' on $PATH and TLDR_ROOT to be a Git repository).
    -S, --sync
        Synchronize each translation's alias page (if exists) with that of the English page.
    -n, --dry-run
        Show what changes would be made without actually modifying the page.


Examples:
    1. Add 'vi' as an alias page of 'vim':
       python3 scripts/set-alias-page.py -p common/vi vim

    2. Read English alias pages and synchronize them into all translations:
       python3 scripts/set-alias-page.py -S

    3. Read English alias pages and show what changes would be made:
       python3 scripts/set-alias-page.py -Sn
       python3 scripts/set-alias-page.py --sync --dry-run

    4. Read English alias pages and synchronize them for Brazilian Portuguese pages only:
       python3 scripts/set-alias-page.py -S -l pt_BR
       python3 scripts/set-alias-page.py --sync --language pt_BR
"""

import argparse
import os
import re
import subprocess

IGNORE_FILES = (".DS_Store", "tldr.md", "aria2.md")


def get_tldr_root():
    """
    Get the path of local tldr repository for environment variable TLDR_ROOT.
    """

    # If this script is running from tldr/scripts, the parent's parent is the root
    f = os.path.normpath(__file__)
    if f.endswith("tldr/scripts/set-alias-page.py"):
        return os.path.dirname(os.path.dirname(f))

    if "TLDR_ROOT" in os.environ:
        return os.environ["TLDR_ROOT"]
    else:
        raise SystemExit(
            "\x1b[31mPlease set TLDR_ROOT to the location of a clone of https://github.com/tldr-pages/tldr.\x1b[0m"
        )


def get_templates(root):
    """
    Get all alias page translation templates from
    TLDR_ROOT/contributing-guides/translation-templates/alias-pages.md.

    Parameters:
    root (string): The path of local tldr repository, i.e., TLDR_ROOT.

    Returns:
    dict of (str, str): Language labels map to alias page templates.
    """

    template_file = os.path.join(
        root, "contributing-guides/translation-templates/alias-pages.md"
    )
    with open(template_file, encoding="utf-8") as f:
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


def get_alias_page(file):
    """
    Determine whether the given file is an alias page.

    Parameters:
    file (string): Path to a page

    Returns:
    str: "" If the file doesn't exit or is not an alias page,
         otherwise return what command the alias stands for.
    """

    if not os.path.isfile(file):
        return ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if match := re.search(r"^`tldr (.+)`", line):
                return match[1]
    return ""


def set_alias_page(file, command, dry_run=False, language_to_update=""):
    """
    Write an alias page to disk.

    Parameters:
    file (string): Path to an alias page
    command (string): The command that the alias stands for.
    dry_run (bool): Whether to perform a dry-run, i.e. only show the changes that would be made.
    language_to_update (string): Optionally, the language of the translation to be updated.

    Returns:
    str: Execution status
         "" if the alias page standing for the same command already exists.
         "\x1b[36mpage added" if it's a new alias page.
         "\x1b[34mpage updated" if the command updates.
    """

    # compute locale
    pages_dir = os.path.basename(os.path.dirname(os.path.dirname(file)))
    if "." in pages_dir:
        _, locale = pages_dir.split(".")
    else:
        locale = "en"
    if locale not in templates or (
        language_to_update != "" and locale != language_to_update
    ):
        return ""

    # Test if the alias page already exists
    orig_command = get_alias_page(file)
    if orig_command == command:
        return ""

    if orig_command == "":
        status_prefix = "\x1b[36m"
        action = "added"
    else:
        status_prefix = "\x1b[34m"
        action = "updated"

    if dry_run:
        status = f"page will be {action}"
    else:
        status = f"page {action}"

    status = f"{status_prefix}{status}\x1b[0m"

    if not dry_run:  # Only write to the file during a non-dry-run
        alias_name, _ = os.path.splitext(os.path.basename(file))
        text = (
            templates[locale]
            .replace("example", alias_name, 1)
            .replace("example", command)
        )
        os.makedirs(os.path.dirname(file), exist_ok=True)
        with open(file, "w", encoding="utf-8") as f:
            f.write(text)

    return status


def sync(
    root, pages_dirs, alias_name, orig_command, dry_run=False, language_to_update=""
):
    """
    Synchronize an alias page into all translations.

    Parameters:
    root (str): TLDR_ROOT
    pages_dirs (list of str): Strings of page entry and platform, e.g. "page.fr/common".
    alias_name (str): An alias command with .md extension like "vi.md".
    orig_command (string): An Original command like "vim".
    dry_run (bool): Whether to perform a dry-run, i.e. only show the changes that would be made.
    language_to_update (string): Optionally, the language of the translation to be updated.

    Returns:
    list: A list of paths to be staged into git, using by --stage option.
    """
    rel_paths = []
    for page_dir in pages_dirs:
        path = os.path.join(root, page_dir, alias_name)
        status = set_alias_page(path, orig_command, dry_run, language_to_update)
        if status != "":
            rel_path = path.replace(f"{root}/", "")
            rel_paths.append(rel_path)
            print(f"\x1b[32m{rel_path} {status}\x1b[0m")
    return rel_paths


def main():
    parser = argparse.ArgumentParser(
        description="Sets the alias page for all translations of a page"
    )
    parser.add_argument(
        "-p",
        "--page",
        type=str,
        required=False,
        default="",
        help='page name in the format "platform/alias_command.md"',
    )
    parser.add_argument(
        "-l",
        "--language",
        type=str,
        required=False,
        default="",
        help='language in the format "ll" or "ll_CC" (e.g. "fr" or "pt_BR")',
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
        help="synchronize each translation's alias page (if exists) with that of English page",
    )
    parser.add_argument(
        "-n",
        "--dry-run",
        action="store_true",
        default=False,
        help="show what changes would be made without actually modifying the pages",
    )
    parser.add_argument("command", type=str, nargs="?", default="")
    args = parser.parse_args()

    root = get_tldr_root()

    # A dictionary of all alias page translations
    global templates
    templates = get_templates(root)
    pages_dirs = [d for d in os.listdir(root) if d.startswith("pages")]
    rel_paths = []

    # Use '--page' option
    if args.page != "":
        if not args.page.lower().endswith(".md"):
            args.page = f"{args.page}.md"

        target_paths = [os.path.join(root, p, args.page) for p in pages_dirs]
        target_paths.sort()

        for path in target_paths:
            rel_path = path.replace(f"{root}/", "")
            rel_paths.append(rel_path)
            status = set_alias_page(path, args.command, args.language)
            if status != "":
                print(f"\x1b[32m{rel_path} {status}\x1b[0m")

    # Use '--sync' option
    elif args.sync:
        pages_dirs.remove("pages")
        en_page = os.path.join(root, "pages")
        platforms = [i for i in os.listdir(en_page) if i not in IGNORE_FILES]
        for platform in platforms:
            platform_path = os.path.join(en_page, platform)
            commands = [
                f"{platform}/{p}"
                for p in os.listdir(platform_path)
                if p not in IGNORE_FILES
            ]
            for command in commands:
                orig_command = get_alias_page(os.path.join(root, "pages", command))
                if orig_command != "":
                    rel_paths += sync(
                        root,
                        pages_dirs,
                        command,
                        orig_command,
                        args.dry_run,
                        args.language,
                    )

    # Use '--stage' option
    if args.stage and not args.dry_run:
        subprocess.call(["git", "add", *rel_paths], cwd=root)


if __name__ == "__main__":
    main()
