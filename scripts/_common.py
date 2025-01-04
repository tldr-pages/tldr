#!/usr/bin/env python3
# SPDX-License-Identifier: MIT

"""
A Python file that makes some commonly used functions available for other scripts to use.
"""

from enum import Enum
from pathlib import Path
from unittest.mock import patch
import shutil
import os
import argparse
import subprocess

IGNORE_FILES = (".DS_Store",)


class Colors(str, Enum):
    def __str__(self):
        return str(
            self.value
        )  # make str(Colors.COLOR) return the ANSI code instead of an Enum object

    RED = "\x1b[31m"
    GREEN = "\x1b[32m"
    BLUE = "\x1b[34m"
    CYAN = "\x1b[36m"
    RESET = "\x1b[0m"


def test_ignore_files():
    assert IGNORE_FILES == (".DS_Store",)
    assert ".DS_Store" in IGNORE_FILES
    assert "tldr.md" not in IGNORE_FILES


def get_tldr_root(lookup_path: Path = None) -> Path:
    """
    Get the path of the local tldr repository, looking for it in each part of the given path. If it is not found, the path in the environment variable TLDR_ROOT is returned.

    Parameters:
    lookup_path (Path): the path to search for the tldr root. By default, the path of the script.

    Returns:
    Path: the local tldr repository.
    """

    if lookup_path is None:
        absolute_lookup_path = Path(__file__).resolve()
    else:
        absolute_lookup_path = Path(lookup_path).resolve()
    if (
        tldr_root := next(
            (path for path in absolute_lookup_path.parents if path.name == "tldr"), None
        )
    ) is not None:
        return tldr_root
    elif "TLDR_ROOT" in os.environ:
        return Path(os.environ["TLDR_ROOT"])
    raise SystemExit(
        f"{Colors.RED}Please set the environment variable TLDR_ROOT to the location of a clone of https://github.com/tldr-pages/tldr{Colors.RESET}"
    )


def test_get_tldr_root():
    tldr_root = get_tldr_root("/path/to/tldr/scripts/test_script.py")
    assert tldr_root == Path("/path/to/tldr")

    # Set TLDR_ROOT in the environment
    os.environ["TLDR_ROOT"] = "/path/to/tldr_clone"

    tldr_root = get_tldr_root("/tmp")
    assert tldr_root == Path("/path/to/tldr_clone")

    del os.environ["TLDR_ROOT"]

    # Remove TLDR_ROOT from the environment
    original_env = os.environ.pop("TLDR_ROOT", None)

    # Check if SystemExit is raised
    raised = False
    try:
        get_tldr_root("/tmp")
    except SystemExit:
        raised = True
    assert raised

    # Restore the original values
    if original_env is not None:
        os.environ["TLDR_ROOT"] = original_env


def get_pages_dir(root: Path) -> list[Path]:
    """
    Get all pages directories.

    Parameters:
    root (Path): the path to search for the pages directories.

    Returns:
    list (list of Path's): Path's of page entry and platform, e.g. "page.fr/common".
    """

    return [d for d in root.iterdir() if d.name.startswith("pages")]


def test_get_pages_dir():
    # Create temporary directories with names starting with "pages"

    root = Path("test_root")

    shutil.rmtree(root, True)

    root.mkdir(exist_ok=True)

    # Create temporary directories with names that do not start with "pages"
    (root / "other_dir_1").mkdir(exist_ok=True)
    (root / "other_dir_2").mkdir(exist_ok=True)

    # Call the function and verify that it returns an empty list
    result = get_pages_dir(root)
    assert result == []

    (root / "pages").mkdir(exist_ok=True)
    (root / "pages.fr").mkdir(exist_ok=True)
    (root / "other_dir").mkdir(exist_ok=True)

    # Call the function and verify the result
    result = get_pages_dir(root)
    expected = [root / "pages", root / "pages.fr"]
    assert result.sort() == expected.sort()  # the order differs on Unix / macOS

    shutil.rmtree(root, True)


def get_target_paths(page: Path, pages_dirs: Path) -> list[Path]:
    """
    Get all paths in all languages that match the page.

    Parameters:
    page (Path): the page to search for.

    Returns:
    list (list of Path's): A list of Path's.
    """

    target_paths = []

    if not page.lower().endswith(".md"):
        page = f"{page}.md"
    arg_platform, arg_page = page.split("/")

    for pages_dir in pages_dirs:
        page_path = pages_dir / arg_platform / arg_page

        if not page_path.exists():
            continue
        target_paths.append(page_path)

    target_paths.sort()

    return target_paths


def test_get_target_paths():
    root = Path("test_root")

    shutil.rmtree(root, True)

    root.mkdir(exist_ok=True)

    shutil.os.makedirs(root / "pages" / "common")
    shutil.os.makedirs(root / "pages.fr" / "common")

    file_path = root / "pages" / "common" / "tldr.md"
    with open(file_path, "w"):
        pass

    file_path = root / "pages.fr" / "common" / "tldr.md"
    with open(file_path, "w"):
        pass

    target_paths = get_target_paths("common/tldr", get_pages_dir(root))
    for path in target_paths:
        rel_path = "/".join(path.parts[-3:])
        print(rel_path)

    shutil.rmtree(root, True)


def get_locale(path: Path) -> str:
    """
    Get the locale from the path.

    Parameters:
    path (Path): the path to extract the locale.

    Returns:
    str: a POSIX Locale Name in the form of "ll" or "ll_CC" (e.g. "fr" or "pt_BR").
    """

    # compute locale
    pages_dirname = path.parents[1].name
    if "." in pages_dirname:
        _, locale = pages_dirname.split(".")
    else:
        locale = "en"

    return locale


def test_get_locale():
    assert get_locale(Path("path/to/pages.fr/common/tldr.md")) == "fr"

    assert get_locale(Path("path/to/pages/common/tldr.md")) == "en"

    assert get_locale(Path("path/to/other/common/tldr.md")) == "en"


def get_status(action: str, dry_run: bool, type: str) -> str:
    """
    Get a colored status line.

    Parameters:
    action (str): The action to perform.
    dry_run (bool): Whether to perform a dry-run.
    type (str): The kind of object to modify (alias, link).

    Returns:
    str: A colored line
    """

    match action:
        case "added":
            start_color = Colors.CYAN
        case "updated":
            start_color = Colors.BLUE
        case _:
            start_color = Colors.RED

    if dry_run:
        status = f"{type} would be {action}"
    else:
        status = f"{type} {action}"

    return create_colored_line(start_color, status)


def test_get_status():
    # Test dry run status
    assert (
        get_status("added", True, "alias")
        == f"{Colors.CYAN}alias would be added{Colors.RESET}"
    )
    assert (
        get_status("updated", True, "link")
        == f"{Colors.BLUE}link would be updated{Colors.RESET}"
    )

    # Test non-dry run status
    assert (
        get_status("added", False, "alias") == f"{Colors.CYAN}alias added{Colors.RESET}"
    )
    assert (
        get_status("updated", False, "link")
        == f"{Colors.BLUE}link updated{Colors.RESET}"
    )

    # Test default color for unknown action
    assert (
        get_status("unknown", True, "alias")
        == f"{Colors.RED}alias would be unknown{Colors.RESET}"
    )


def create_colored_line(start_color: str, text: str) -> str:
    """
    Create a colored line.

    Parameters:
    start_color (str): The color for the line.
    text (str): The text to display.

    Returns:
    str: A colored line
    """

    return f"{start_color}{text}{Colors.RESET}"


def test_create_colored_line():
    assert (
        create_colored_line(Colors.CYAN, "TLDR") == f"{Colors.CYAN}TLDR{Colors.RESET}"
    )
    assert create_colored_line("Hello", "TLDR") == f"HelloTLDR{Colors.RESET}"


def create_argument_parser(description: str) -> argparse.ArgumentParser:
    """
    Create an argument parser that can be extended.

    Parameters:
    description (str): The description for the argument parser

    Returns:
    ArgumentParser: an argument parser.
    """

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        "-p",
        "--page",
        type=str,
        default="",
        help='page name in the format "platform/alias_command.md"',
    )
    parser.add_argument(
        "-S",
        "--sync",
        action="store_true",
        default=False,
        help="synchronize each translation's alias page (if exists) with that of English page",
    )
    parser.add_argument(
        "-l",
        "--language",
        type=str,
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
        "-n",
        "--dry-run",
        action="store_true",
        default=False,
        help="show what changes would be made without actually modifying the pages",
    )

    return parser


def test_create_argument_parser():
    description = "Test argument parser"
    parser = create_argument_parser(description)

    assert isinstance(parser, argparse.ArgumentParser)
    assert parser.description == description

    # Check if each expected argument is added with the correct configurations
    arguments = [
        ("-p", "--page", str, ""),
        ("-l", "--language", str, ""),
        ("-s", "--stage", None, False),
        ("-S", "--sync", None, False),
        ("-n", "--dry-run", None, False),
    ]
    for short_flag, long_flag, arg_type, default_value in arguments:
        action = parser._option_string_actions[short_flag]  # Get action for short flag
        assert action.dest.replace("_", "-") == long_flag.lstrip(
            "-"
        )  # Check destination name
        assert action.type == arg_type  # Check argument type
        assert action.default == default_value  # Check default value


def stage(paths: list[Path]):
    """
    Stage the given paths using Git.

    Parameters:
    paths (list of Paths): the list of Path's to stage using Git.

    """
    subprocess.call(["git", "add", *(path.resolve() for path in paths)])


@patch("subprocess.call")
def test_stage(mock_subprocess_call):
    paths = [Path("/path/to/file1"), Path("/path/to/file2")]

    # Call the stage function
    stage(paths)

    # Verify that subprocess.call was called with the correct arguments
    mock_subprocess_call.assert_called_once_with(["git", "add", *paths])
