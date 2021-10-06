#!/usr/bin/env python3
# SPDX-License-Identifier: MIT

import argparse
import os
import re
import subprocess
import sys

IGNORE_FILES = (".DS_Store", "tldr.md")


def get_tldr_root():
    # If this script is running from tldr/scripts, the parent's parent is the root
    f = os.path.normpath(__file__)
    if f.endswith("tldr/scripts/set-more-info-link.py"):
        return os.path.dirname(os.path.dirname(f))

    if "TLDR_ROOT" in os.environ:
        return os.environ["TLDR_ROOT"]
    else:
        print(
            "\x1b[31mPlease set TLDR_ROOT to the location of a clone of https://github.com/tldr-pages/tldr."
        )
        sys.exit(1)


def get_templates():
    template_file = os.path.join(
        get_tldr_root(), "contributing-guides/translation-templates/alias-pages.md"
    )
    with open(template_file) as f:
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


# A dictionary of all alias page translations
templates = get_templates()


def get_alias_page(file):
    if not os.path.isfile(file):
        return ""

    with open(file) as f:
        lines = f.readlines()
    for line in lines:
        if re.search(r"^`tldr ", line):
            return re.search("`tldr (.+)`", line).group(1)
    return ""


def set_alias_page(file, command):
    # compute locale
    pages_dir = os.path.basename(os.path.dirname(os.path.dirname(file)))
    if "." in pages_dir:
        _, locale = pages_dir.split(".")
    else:
        locale = "en"
    if locale not in templates:
        return ""

    # Test if the alias page already exists
    orig_command = get_alias_page(file)
    if orig_command == command:
        return ""
    elif orig_command == "":
        status = "\x1b[36mpage added"
    else:
        status = "\x1b[34mpage updated"

    alias_name = os.path.basename(file).strip(".md")
    text = (
        templates[locale].replace("example", alias_name, 1).replace("example", command)
    )
    os.makedirs(os.path.dirname(file), exist_ok=True)
    with open(file, "w") as f:
        f.write(text)

    return status


def sync(root, pages_dirs, alias_name, orig_command):
    rel_paths = []
    for page_dir in pages_dirs:
        path = os.path.join(root, page_dir, alias_name)
        status = set_alias_page(path, orig_command)
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
    parser.add_argument("command", type=str, nargs="?", default="")
    args = parser.parse_args()

    root = get_tldr_root()
    pages_dirs = [d for d in os.listdir(root) if d.startswith("pages")]

    rel_paths = []

    # Use '--page' option
    if args.page != "":
        target_paths = []

        if not args.page.lower().endswith(".md"):
            args.page = f"{args.page}.md"

        target_paths = [os.path.join(root, p, args.page) for p in pages_dirs]

        target_paths.sort()

        for path in target_paths:
            rel_path = path.replace(f"{root}/", "")
            rel_paths.append(rel_path)
            status = set_alias_page(path, args.command)
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
                    rel_paths += sync(root, pages_dirs, command, orig_command)

    if args.stage:
        subprocess.call(["git", "add", *rel_paths], cwd=root)


if __name__ == "__main__":
    main()
