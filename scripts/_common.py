#!/usr/bin/env python3
# SPDX-License-Identifier: MIT

"""
A Python file that makes some commonly used functions available for other scripts to use.
"""

from pathlib import Path
import os
import argparse
import subprocess

IGNORE_FILES = (".DS_Store",)


def get_tldr_root() -> Path:
    """
    Get the path of local tldr repository for environment variable TLDR_ROOT.
    """

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


def get_pages_dir(root: Path):
    return [d for d in root.iterdir() if d.name.startswith("pages")]


def get_locale(path: Path) -> str:
    """
    Get the locale from the path.
    """

    # compute locale
    pages_dirname = path.parents[1].name
    if "." in pages_dirname:
        _, locale = pages_dirname.split(".")
    else:
        locale = "en"

    return locale


def get_status(action: str, dry_run: bool, type: str) -> str:
    """
    Get a colored status line.

    Parameters:
    action (str): The action to perform.
    dry_run (bool): Whether to perform a dry-run.
    type (str): The kind of object to modify (alias, link).

    Returns:
    str: A coloured line
    """

    match action:
        case "added":
            status_prefix = "\x1b[36m"  # Cyan color
        case "updated":
            status_prefix = "\x1b[34m"  # Blue color
        case _:
            status_prefix = "\x1b[31m"  # Red color (default)

    if dry_run:
        status = f"{type} will be {action}"
    else:
        status = f"{type} {action}"

    return create_colored_line(status_prefix, status)


def sync(
    root: Path,
    pages_dirs: list[str],
    name: str,
    command: str,
    update_function,
    dry_run=False,
) -> list[str]:
    """
    Synchronize a page into all translations.

    Parameters:
    root (str): TLDR_ROOT
    pages_dirs (list of str): Strings of page entry and platform, e.g. "page.fr/common".
    name (str): An alias command with .md extension like "vi.md".
    command (str): The command to sync.
    update_function: The function to call (set_link or set_alias)
    dry_run (bool): Whether to perform a dry-run.

    Returns:
    list: A list of paths to be staged into git, using by --stage option.
    """
    paths = []
    for page_dir in pages_dirs:
        path = root / page_dir / name
        if path.exists():
            rel_path = "/".join(path.parts[-3:])
            status = update_function(path, command, dry_run)
            if status != "":
                paths.append(path)
                print(create_colored_line("\x1b[32m", f"{rel_path} {status}"))
    return paths


def create_colored_line(start_colour: str, text: str) -> str:
    """
    ...
    """

    return f"{start_colour}{text}\x1b[0m"


def create_argument_parser(description: str) -> argparse.ArgumentParser:
    """
    Create an argument parser that can be extended.
    """

    parser = argparse.ArgumentParser(description=description)
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

    return parser


def stage(paths: list[str], cwd: Path):
    subprocess.call(["git", "add", *paths], cwd=cwd)
