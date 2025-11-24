#!/usr/bin/env python3
# SPDX-License-Identifier: MIT

"""
A Python script to generate or update alias pages.

Disclaimer: This script generates a lot of false positives so it isn't suggested to use the sync option. If used, only stage changes and commit verified changes for your language by using -l LANGUAGE.

Note: If the current directory or one of its parents is called "tldr", the script will assume it is the tldr root, i.e., the directory that contains a clone of https://github.com/tldr-pages/tldr
If you aren't, the script will use TLDR_ROOT as the tldr root. Also, ensure 'git' is available.

Note: This script uses an interactive prompt instead of positional arguments to:
- Prevent argument parsing errors with command names containing dashes (e.g. 'pacman -S')
- Provide clearer guidance for required inputs
- Allow for input validation before page creation

Usage:
    python3 scripts/set-alias-page.py [-p PAGE] [-S] [-l LANGUAGE] [-s] [-n]

Options:
    -p, --page PAGE
        Specify the alias page in the format "platform/alias_command.md".
        This will start an interactive prompt to create/update the page.
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
       python3 scripts/set-alias-page.py --page osx/gsum
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
from dataclasses import dataclass
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


@dataclass
class Config:
    """Global configuration for the script"""

    root: Path
    pages_dirs: list[Path]
    templates: dict[str, str]
    dry_run: bool = False
    language: str = ""


@dataclass
class AliasPageContent:
    """Content of an alias page"""

    title: str
    original_command: str
    documentation_command: str


@dataclass
class AliasPage:
    """Represents an alias page with its path and content"""

    page_path: str
    content: AliasPageContent


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
    page_content: AliasPageContent,
) -> str:
    """
    Generate alias page content by replacing placeholders in the template.

    Parameters:
        template_content (str): The markdown template for the specific language.
        page_content (AliasPageContent): The content of the alias page

    Returns:
        str: The complete markdown content for the alias page.
    """

    template_command = "example"

    # Replace placeholders in template with actual values
    result = template_content.replace(template_command, page_content.title, 1)
    result = result.replace(template_command, page_content.original_command, 1)
    result = result.replace(template_command, page_content.documentation_command)

    return result


def set_alias_page(
    path: Path,
    page_content: AliasPageContent,
) -> str:
    """
    Write an alias page to disk.

    Parameters:
        path (Path): Path to an alias page
        page_content (AliasPageContent): The content to write to the page

    Returns:
        str: Execution status
             "" if the alias page standing for the same command already exists or if the locale does not match language_to_update.
             "\x1b[36mpage added"
             "\x1b[34mpage updated"
             "\x1b[36mpage would be added"
             "\x1b[34mpage would updated"
    """

    locale = get_locale(path)
    if locale not in config.templates or (
        config.language != "" and locale != config.language
    ):
        return ""

    # Get existing alias command from the locale page
    existing_locale_page_content = get_alias_command_in_page(
        path, get_locale_alias_pattern(locale)
    )

    if (
        existing_locale_page_content.documentation_command
        == page_content.documentation_command
    ):
        return ""

    new_locale_page_content = generate_alias_page_content(
        config.templates[locale],
        page_content,
    )

    # Determine status and write file
    status = get_status(
        "added" if not path.exists() else "updated",
        config.dry_run,
        "page",
    )

    if not config.dry_run:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as f:
            f.write(new_locale_page_content)

    return status


def get_locale_alias_pattern(locale: str) -> str:
    """Get alias pattern from template"""

    template_line = re.search(r">.*`example`", config.templates[locale]).group(0)
    locale_alias_pattern = template_line[2 : template_line.find("`example`")].strip()
    return locale_alias_pattern


def get_alias_command_in_page(path: Path, alias_pattern: str) -> AliasPageContent:
    """
    Determine whether the given path is an alias page.

    Returns:
        AliasPageContent: The page content, or empty strings if not an alias page
    """

    if not path.exists():
        return AliasPageContent(title="", original_command="", documentation_command="")

    with path.open(encoding="utf-8") as f:
        content = f.read()

    lines = content.splitlines()

    title = next((line.strip("# \n") for line in lines if line.startswith("# ")), "")

    command_lines = [line for line in lines if "`" in line]

    if len(command_lines) != 2 or not title:
        return AliasPageContent(title="", original_command="", documentation_command="")

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

    return AliasPageContent(
        title=title,
        original_command=original_command,
        documentation_command=documentation_command,
    )


def sync_alias_page_to_locale(pages_dir: Path, alias_page: AliasPage) -> list[Path]:
    """
    Synchronize an alias page into a specific locale directory.

    Parameters:
        pages_dir (Path): Directory containing pages for a specific locale
        alias_page (AliasPage): The alias page to sync

    Returns:
        list[Path]: List of paths that were modified
    """

    paths = []
    path = config.root / pages_dir / alias_page.page_path
    status = set_alias_page(path, alias_page.content)
    if status != "":
        rel_path = "/".join(path.parts[-3:])
        paths.append(rel_path)
        print(create_colored_line(Colors.GREEN, f"{rel_path} {status}"))
    return paths


def get_english_alias_pages(en_path: Path) -> list[AliasPage]:
    """
    Get all English alias pages with their commands.

    Parameters:
        en_path (Path): Path to English pages directory

    Returns:
        list[AliasPage]: List of alias pages with their content
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
        page_paths = [
            f"{platform}/{page.name}"
            for page in platform_path.iterdir()
            if page.name not in IGNORE_FILES
        ]

        # Check each command if it's an alias
        for page_path in page_paths:
            page_content = get_alias_command_in_page(en_path / page_path, alias_pattern)
            if page_content.original_command:
                alias_pages.append(AliasPage(page_path=page_path, content=page_content))

    return alias_pages


def prompt_alias_page_info(page_path: str) -> AliasPageContent:
    """
    Prompt user for alias page content.

    Returns:
        AliasPageContent: The collected page content
    """

    en_path = config.root / "pages"
    if not page_path.lower().endswith(".md"):
        page_path = f"{page_path}.md"
    exists = (en_path / page_path).exists()

    print(f"\n{'Updating' if exists else 'Creating new'} alias page...")
    print(create_colored_line(Colors.CYAN, f"Page path: {page_path}"))

    print(
        create_colored_line(
            Colors.BLUE,
            "\nThe title will be used in the first line of the page after '#'",
        )
    )
    print(create_colored_line(Colors.GREEN, "Example: npm run-script"))
    page_name = Path(page_path).stem
    title = input(
        create_colored_line(
            Colors.CYAN, f"Enter page title (press Enter to use {page_name}): "
        )
    ).strip()
    if not title:
        title = page_name

    print(
        create_colored_line(
            Colors.BLUE,
            "\nThe original command will appear in 'This command is an alias of `command`'",
        )
    )
    print(create_colored_line(Colors.GREEN, "Example: npm run"))
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
    print(create_colored_line(Colors.GREEN, "Example: npm run"))
    documentation_command = input(
        create_colored_line(
            Colors.CYAN,
            f"Enter documentation command (press Enter to use {original_command}): ",
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
            Colors.GREEN, f"\n> This command is an alias of `{original_command}`."
        )
    )
    print(
        create_colored_line(
            Colors.GREEN, "\n- View documentation for the original command:"
        )
    )
    print(create_colored_line(Colors.GREEN, f"\n`tldr {documentation_command}`"))

    response = (
        input(create_colored_line(Colors.CYAN, "\nProceed? [Y/n] ")).lower().strip()
    )
    if response and response not in ["y", "yes"]:
        raise SystemExit(create_colored_line(Colors.RED, "Cancelled by user"))

    return AliasPageContent(
        title=title,
        original_command=original_command,
        documentation_command=documentation_command,
    )


def main():
    parser = create_argument_parser(
        "Sets the alias page for all translations of a page"
    )
    args = parser.parse_args()
    root = get_tldr_root()
    pages_dirs = get_pages_dir(root)
    templates = get_templates(root)

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
        page_info = prompt_alias_page_info(args.page)
        target_paths += get_target_paths(
            args.page, config.pages_dirs, check_exists=False
        )

        for path in target_paths:
            rel_path = "/".join(path.parts[-3:])
            status = set_alias_page(path, page_info)
            if status != "":
                print(create_colored_line(Colors.GREEN, f"{rel_path} {status}"))

    # Use '--sync' option
    elif args.sync:
        en_path = config.root / "pages"
        pages_dirs = config.pages_dirs.copy()
        pages_dirs.remove(en_path)

        alias_pages = get_english_alias_pages(en_path)

        for alias_page in alias_pages:
            for pages_dir in pages_dirs:
                target_paths.extend(sync_alias_page_to_locale(pages_dir, alias_page))

    # Use '--stage' option
    if args.stage and not config.dry_run and len(target_paths) > 0:
        stage(target_paths)


if __name__ == "__main__":
    main()
