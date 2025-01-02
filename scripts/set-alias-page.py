#!/usr/bin/env python3
# SPDX-License-Identifier: MIT

"""
A Python script to generate or update alias pages.

Disclaimer: This script generates a lot of false positives so it isn't suggested to use the sync option. If used, only stage changes and commit verified changes for your language by using -l LANGUAGE.

Note: If the current directory or one of its parents is called "tldr", the script will assume it is the tldr root, i.e., the directory that contains a clone of https://github.com/tldr-pages/tldr
If you aren't, the script will use TLDR_ROOT as the tldr root. Also, ensure 'git' is available.

Usage:
    python3 scripts/set-alias-page.py [-P PAGE] [-S] [-l LANGUAGE] [-s] [-n] [ORIGINAL_CMD] [DOC_CMD]

Options:
    -P, --page PAGE
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
    ORIGINAL_CMD          The command to be set as the alias command.
    DOC_CMD               The command to view documentation (defaults to ORIGINAL_CMD)

Examples:
    1. Add 'gsum' as an alias page of GNU 'sum' with documentation at '-p linux sum':
       python3 scripts/set-alias-page.py -P osx/gsum sum "-p linux sum"
       * osx/gsum: the alias page to create
       * sum: original_command (GNU sum command that gsum is an alias of)
       * "-p linux sum": documentation_command (view documentation in linux/sum page)

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


def generate_alias_page_content(
    template_content: str,
    command_name: str,
    original_command: str,
    documentation_command: str,
) -> str:
    """
    Generate alias page content by replacing placeholders in the template.

    Parameters:
    template_content (str): The markdown template for the specific language.
    command_name (str): The name of the alias command (used in page title).
    original_command (str): The original command that this alias refers to.
    documentation_command (str): The tldr command to view the documentation.

    Returns:
    str: The complete markdown content for the alias page.
    """
    # Format command name for title (replace first dash with space)
    formatted_command_name = (
        command_name.replace("-", " ", 1) if "-" in command_name else command_name
    )

    # Replace placeholders in template with actual values
    page_content = template_content.replace("example", formatted_command_name, 1)
    page_content = page_content.replace("example", original_command, 1)
    page_content = page_content.replace("example", documentation_command)

    return page_content


def set_alias_page(
    path: Path,
    original_command: str,
    documentation_command: str,
    dry_run: bool = False,
    language_to_update: str = "",
) -> str:
    """
    Write an alias page to disk.

    Parameters:
    path (string): Path to an alias page
    original_command (str): The command that the alias stands for.
    documentation_command (str): The command to view documentation.
    dry_run (bool): Whether to perform a dry-run.
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
        return ""

    formatted_command_name = path.stem

    locale_alias_pattern = get_locale_alias_pattern(locale)

    # Get existing alias command from the locale page
    existing_original_command, existing_documentation_command = (
        get_alias_command_in_page(path, locale_alias_pattern)
    )

    if (
        existing_original_command == original_command
        and existing_documentation_command == documentation_command
    ):
        return ""

    # Generate the new locale page content
    locale_page_content = generate_alias_page_content(
        templates[locale],
        formatted_command_name,
        original_command,
        documentation_command,
    )

    # Determine status and write file
    status = get_status(
        "added" if not path.exists() else "updated",
        dry_run,
        "page",
    )

    if not dry_run:  # Only write to the path during a non-dry-run
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as f:
            f.write(locale_page_content)

    return status


def get_locale_alias_pattern(locale: str) -> str:
    """Get alias pattern from template"""
    template_line = re.search(r">.*`example`", templates[locale]).group(0)
    locale_alias_pattern = template_line[2 : template_line.find("`example`")].strip()
    return locale_alias_pattern


def get_alias_command_in_page(path: Path, alias_pattern: str) -> tuple[str, str]:
    """
    Determine whether the given path is an alias page.

    Parameters:
    path (Path): Path to a page
    alias_pattern (str): The pattern that defines an alias in the language
                        (e.g. "This command is an alias of" for English, "이 명령은" for Korean, "このコマンドは" for Japanese)

    Returns:
    tuple[str, str]: A tuple of (original_command, documentation_command) where:
        original_command: The command from alias declaration line
        documentation_command: The command from "tldr" line
        Returns ("", "") if the path doesn't exist or is not an alias page
    """
    if not path.exists():
        return ("", "")

    with path.open(encoding="utf-8") as f:
        content = f.read()

    command_lines = [line for line in content.splitlines() if "`" in line]

    if len(command_lines) != 2:
        return ("", "")

    original_command = ""
    documentation_command = ""

    alias_line = next((line for line in command_lines if alias_pattern in line), None)
    if alias_line:
        description_match = re.search(r"`([^`]+)`", alias_line)
        if description_match:
            original_command = description_match[1]

    if not original_command:
        return ("", "")

    tldr_line = next(
        (line for line in command_lines if line.strip().startswith("`tldr")), None
    )
    if tldr_line:
        tldr_match = re.search(r"`tldr (.+)`", tldr_line.strip())
        if tldr_match:
            documentation_command = tldr_match[1]

    if not documentation_command:
        return ("", "")

    return (original_command, documentation_command)


def sync(
    root: Path,
    pages_dirs: list[Path],
    alias_name: str,
    original_command: str,
    documentation_command: str,
    dry_run: bool = False,
    language_to_update: str = "",
) -> list[Path]:
    """
    Synchronize an alias page into all translations.

    Parameters:
    root (Path): TLDR_ROOT
    pages_dirs (list of Path's): Path's of page entry and platform, e.g. "page.fr/common".
    alias_name (str): An alias command with .md extension like "vi.md".
    original_command (str): The original command that this alias refers to.
    documentation_command (str): The command to view the documentation.
    dry_run (bool): Whether to perform a dry-run.
    language_to_update (str): Optionally, the language of the translation to be updated.

    Returns:
    list (list of Path's): A list of Path's to be staged into git, using by --stage option.
    """
    paths = []
    for page_dir in pages_dirs:
        path = root / page_dir / alias_name
        status = set_alias_page(
            path, original_command, documentation_command, dry_run, language_to_update
        )
        if status != "":
            rel_path = "/".join(path.parts[-3:])
            paths.append(rel_path)
            print(create_colored_line(Colors.GREEN, f"{rel_path} {status}"))
    return paths


def main():
    parser = create_argument_parser(
        "Sets the alias page for all translations of a page"
    )
    parser.add_argument(
        "original_command",
        type=str,
        metavar="ORIGINAL_CMD",
        help="The command that the alias stands for.",
    )
    parser.add_argument(
        "documentation_command",
        type=str,
        nargs="?",
        metavar="DOC_CMD",
        help="The command to view documentation (defaults to ORIGINAL_CMD)",
    )
    args = parser.parse_args()

    if not args.documentation_command:
        args.documentation_command = args.original_command

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
            status = set_alias_page(
                path,
                args.original_command,
                args.documentation_command,
                args.dry_run,
                args.language,
            )
            if status != "":
                print(create_colored_line(Colors.GREEN, f"{rel_path} {status}"))

    # Use '--sync' option
    elif args.sync:
        pages_dirs.remove(root / "pages")
        en_path = root / "pages"
        platforms = [i.name for i in en_path.iterdir() if i.name not in IGNORE_FILES]
        alias_pattern = get_locale_alias_pattern("en")
        for platform in platforms:
            platform_path = en_path / platform
            commands = [
                f"{platform}/{page.name}"
                for page in platform_path.iterdir()
                if page.name not in IGNORE_FILES
            ]
            for command in commands:
                original_command, documentation_command = get_alias_command_in_page(
                    root / "pages" / command, alias_pattern
                )
                if original_command != "":
                    target_paths += sync(
                        root,
                        pages_dirs,
                        command,
                        original_command,
                        documentation_command,
                        args.dry_run,
                        args.language,
                    )

    # Use '--stage' option
    if args.stage and not args.dry_run and len(target_paths) > 0:
        stage(target_paths)


def test_command_parsing_from_file(path: str):
    """
    Test function to check alias command parsing

    Parameters:
    path (str): The path to the alias page
    (e.g. pages/osx/gsum.md)

    Example:
    python3 scripts/set-alias-page.py --test pages/osx/gsum.md
    python3 scripts/set-alias-page.py --test "pages.ko/osx/g[.md"

    Output:
    Testing file: pages/osx/gsum.md
    Content: ...
    Original command: sum
    Documentation command: -p linux sum
    """

    root = get_tldr_root()
    abs_path = root / path

    locale = get_locale(abs_path)

    global templates
    templates = get_templates(root)

    alias_pattern = get_locale_alias_pattern(locale)

    original_command, documentation_command = get_alias_command_in_page(
        abs_path, alias_pattern
    )
    print(f"Testing file: {path}")
    print(f"Content: {abs_path.read_text()}")
    print(f"Original command: {original_command}")
    print(f"Documentation command: {documentation_command}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        test_command_parsing_from_file(sys.argv[2])
    else:
        main()
