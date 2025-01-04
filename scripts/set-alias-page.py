#!/usr/bin/env python3
# SPDX-License-Identifier: MIT

"""
A Python script to generate or update alias pages.

Disclaimer: This script generates a lot of false positives so it isn't suggested to use the sync option. If used, only stage changes and commit verified changes for your language by using -l LANGUAGE.

Note: If the current directory or one of its parents is called "tldr", the script will assume it is the tldr root, i.e., the directory that contains a clone of https://github.com/tldr-pages/tldr
If you aren't, the script will use TLDR_ROOT as the tldr root. Also, ensure 'git' is available.

Usage:
    python3 scripts/set-alias-page.py [-p PAGE] [-S] [-l LANGUAGE] [-s] [-n]

Options:
    -p, --page PAGE
        Specify the alias page in the format "platform/alias_command.md".
        This will start an interactive wizard to create/update the page.
    -S, --sync
        Synchronize each translation's alias page (if exists) with that of the English page.
    -l, --language LANGUAGE
        Specify the language, a POSIX Locale Name in the form of "ll" or "ll_CC" (e.g. "fr" or "pt_BR").
    -s, --stage
        Stage modified pages (requires 'git' on $PATH and TLDR_ROOT to be a Git repository).
    -n, --dry-run
        Show what changes would be made without actually modifying the page.

Examples:
    1. Create a new alias page interactively:
       python3 scripts/set-alias-page.py -p osx/gsum
       This will start a wizard that guides you through creating the page.

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
from dataclasses import dataclass

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
    title: str,
    original_command: str,
    documentation_command: str,
) -> str:
    """
    Generate alias page content by replacing placeholders in the template.

    Parameters:
    template_content (str): The markdown template for the specific language.
    title (str): The title of the alias page
    original_command (str): The original command that this alias refers to.
    documentation_command (str): The tldr command to view the documentation.

    Returns:
    str: The complete markdown content for the alias page.
    """

    # Replace placeholders in template with actual values
    page_content = template_content.replace("example", title, 1)
    page_content = page_content.replace("example", original_command, 1)
    page_content = page_content.replace("example", documentation_command)

    return page_content


def set_alias_page(
    path: Path,
    title: str,
    original_command: str,
    documentation_command: str,
    dry_run: bool = False,
    language_to_update: str = "",
) -> str:
    """
    Write an alias page to disk.

    Parameters:
    path (string): Path to an alias page
    title (str): The title of the alias page
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

    # Get existing alias command from the locale page
    _, _, existing_documentation_command = get_alias_command_in_page(
        path, get_locale_alias_pattern(locale)
    )

    if existing_documentation_command == documentation_command:
        return ""

    # Generate the new locale page content
    locale_page_content = generate_alias_page_content(
        templates[locale],
        title,
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


def get_alias_command_in_page(path: Path, alias_pattern: str) -> tuple[str, str, str]:
    """
    Determine whether the given path is an alias page.

    Parameters:
    path (Path): Path to a page
    alias_pattern (str): The pattern that defines an alias in the language
                        (e.g. "This command is an alias of" for English, "이 명령은" for Korean, "このコマンドは" for Japanese)

    Returns:
    tuple[str, str, str]: A tuple of (title, original_command, documentation_command) where:
        title: The command title from the first line
        original_command: The command from alias declaration line
        documentation_command: The command from "tldr" line
        Returns ("", "", "") if the path doesn't exist or is not an alias page
    """
    if not path.exists():
        return ("", "", "")

    with path.open(encoding="utf-8") as f:
        content = f.read()

    lines = content.splitlines()

    # Get title from first line
    title = next((line.strip("# \n") for line in lines if line.startswith("# ")), "")

    command_lines = [line for line in lines if "`" in line]

    if len(command_lines) != 2 or not title:
        return ("", "", "")

    original_command = ""
    documentation_command = ""

    alias_line = next((line for line in command_lines if alias_pattern in line), None)
    if alias_line:
        description_match = re.search(r"`([^`]+)`", alias_line)
        if description_match:
            original_command = description_match[1]

    tldr_line = next(
        (line for line in command_lines if line.strip().startswith("`tldr")), None
    )
    if tldr_line:
        tldr_match = re.search(r"`tldr (.+)`", tldr_line.strip())
        if tldr_match:
            documentation_command = tldr_match[1]

    return (title, original_command, documentation_command)


@dataclass
class SyncConfig:
    """Configuration for synchronizing alias pages"""

    root: Path
    pages_dirs: list[Path]
    dry_run: bool = False
    language: str = ""


@dataclass
class AliasPage:
    """Represents an alias page with its commands"""

    command: str
    title: str
    original_command: str
    documentation_command: str


def sync(config: SyncConfig, alias_page: AliasPage) -> list[Path]:
    """
    Synchronize an alias page into all translations.

    Parameters:
    config (SyncConfig): Sync configuration
    alias_page (AliasPage): The alias page to sync

    Returns:
    list[Path]: List of paths that were modified
    """
    paths = []
    for page_dir in config.pages_dirs:
        path = config.root / page_dir / alias_page.command
        status = set_alias_page(
            path,
            alias_page.title,
            alias_page.original_command,
            alias_page.documentation_command,
            config.dry_run,
            config.language,
        )
        if status != "":
            rel_path = "/".join(path.parts[-3:])
            paths.append(rel_path)
            print(create_colored_line(Colors.GREEN, f"{rel_path} {status}"))
    return paths


def sync_translations(
    root: Path, pages_dirs: list[Path], dry_run: bool = False, language: str = ""
) -> list[Path]:
    """Synchronize all alias pages with their translations."""
    config = SyncConfig(
        root=root, pages_dirs=pages_dirs, dry_run=dry_run, language=language
    )

    en_path = root / "pages"
    pages_dirs.remove(en_path)

    # Get all English alias pages
    alias_pages = [
        AliasPage(
            command=cmd, title=title, original_command=orig, documentation_command=doc
        )
        for cmd, title, orig, doc in get_english_alias_pages(en_path)
    ]

    # Sync each alias page with translations
    target_paths = []
    for alias_page in alias_pages:
        target_paths.extend(sync(config, alias_page))

    return target_paths


def get_english_alias_pages(en_path: Path) -> list[tuple[str, str, str, str]]:
    """
    Get all English alias pages with their commands.

    Parameters:
    en_path (Path): Path to English pages directory

    Returns:
    list[tuple[str, str, str, str]]: List of (command_path, title, original_command, documentation_command)
    """
    alias_pages = []
    alias_pattern = get_locale_alias_pattern("en")

    # Get all platform directories (common, linux, etc.)
    platforms = [
        page.name for page in en_path.iterdir() if page.name not in IGNORE_FILES
    ]

    # Iterate through each platform
    for platform in platforms:
        platform_path = en_path / platform
        commands = [
            f"{platform}/{page.name}"
            for page in platform_path.iterdir()
            if page.name not in IGNORE_FILES
        ]

        # Check each command if it's an alias
        for command in commands:
            title, original_command, documentation_command = get_alias_command_in_page(
                en_path / command, alias_pattern
            )
            if original_command:  # Only include if it's an alias page
                alias_pages.append(
                    (command, title, original_command, documentation_command)
                )

    return alias_pages


def prompt_alias_page_info(page_path: str) -> tuple[str, str, str]:
    """
    Prompt user for alias page information.

    Parameters:
    page_path (str): The path to the alias page (e.g., "common/test")

    Returns:
    tuple[str, str, str]: (title, original_command, documentation_command)
    """
    print("\nCreating new alias page...")
    print(create_colored_line(Colors.CYAN, f"Page path: {page_path}"))

    print(
        create_colored_line(
            Colors.BLUE,
            "\nThe title will be used in the first line of the page after '#'",
        )
    )
    print(create_colored_line(Colors.GREEN, "Example: '# npm run-script'"))
    title = input(create_colored_line(Colors.CYAN, "Enter page title: ")).strip()
    if not title:
        raise SystemExit(create_colored_line(Colors.RED, "Title cannot be empty"))

    print(
        create_colored_line(
            Colors.BLUE,
            "\nThe original command will appear in 'This command is an alias of `command`'",
        )
    )
    print(
        create_colored_line(
            Colors.GREEN, "Example: 'This command is an alias of `npm run`'"
        )
    )
    original_command = input(
        create_colored_line(Colors.CYAN, "Enter original command: ")
    ).strip()
    if not original_command:
        raise SystemExit(
            create_colored_line(Colors.RED, "Original command cannot be empty")
        )

    print(
        create_colored_line(
            Colors.BLUE,
            "\nThe documentation command will be used in 'tldr command' line",
        )
    )
    print(create_colored_line(Colors.GREEN, "Example: '`tldr npm run`'"))
    documentation_command = input(
        create_colored_line(
            Colors.CYAN,
            "Enter documentation command (press Enter to use original command): ",
        )
    ).strip()

    if not documentation_command:
        documentation_command = original_command

    print("\nSummary:")
    print(f"* Title: {create_colored_line(Colors.CYAN, title)}")
    print(f"* Original command: {create_colored_line(Colors.CYAN, original_command)}")
    print(
        f"* Documentation command: {create_colored_line(Colors.CYAN, documentation_command)}"
    )

    print(create_colored_line(Colors.BLUE, "\nThis will create a page like:"))
    print(create_colored_line(Colors.GREEN, f"# {title}"))
    print(
        create_colored_line(
            Colors.GREEN, f"> This command is an alias of `{original_command}`."
        )
    )
    print(
        create_colored_line(
            Colors.GREEN, "\n- View documentation for the original command:"
        )
    )
    print(create_colored_line(Colors.GREEN, f"`tldr {documentation_command}`"))

    response = (
        input(create_colored_line(Colors.CYAN, "\nProceed? [Y/n] ")).lower().strip()
    )
    if response and response not in ["y", "yes"]:
        raise SystemExit(create_colored_line(Colors.RED, "Cancelled by user"))

    return title, original_command, documentation_command


def main():
    parser = create_argument_parser(
        "Sets the alias page for all translations of a page"
    )

    args = parser.parse_args()

    root = get_tldr_root()

    # A dictionary of all alias page translations
    global templates
    templates = get_templates(root)
    pages_dirs = get_pages_dir(root)

    target_paths = []

    # Use '--page' option
    if args.page != "":
        title, original_command, documentation_command = prompt_alias_page_info(
            args.page
        )
        target_paths += get_target_paths(args.page, pages_dirs)

        for path in target_paths:
            rel_path = "/".join(path.parts[-3:])
            status = set_alias_page(
                path,
                title,
                original_command,
                documentation_command,
                args.dry_run,
                args.language,
            )
            if status != "":
                print(create_colored_line(Colors.GREEN, f"{rel_path} {status}"))

    # Use '--sync' option
    elif args.sync:
        target_paths = sync_translations(
            root=root,
            pages_dirs=pages_dirs,
            dry_run=args.dry_run,
            language=args.language,
        )

    # Use '--stage' option
    if args.stage and not args.dry_run and len(target_paths) > 0:
        stage(target_paths)


if __name__ == "__main__":
    main()
