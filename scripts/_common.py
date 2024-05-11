#!/usr/bin/env python3
# SPDX-License-Identifier: MIT

"""
A Python file that makes some commonly used functions available for other scripts to use.
"""

from pathlib import Path
from unittest.mock import patch
import os
import argparse
import subprocess

IGNORE_FILES = (".DS_Store",)


def get_tldr_root(path=None) -> Path:
    """
    Get the path of local tldr repository for environment variable TLDR_ROOT.
    """

    # If this script is running from tldr/scripts, the parent's parent is the root
    if path is None:
        f = Path(__file__).resolve()
    else:
        f = Path(path).resolve()
    if (
        tldr_root := next((path for path in f.parents if path.name == "tldr"), None)
    ) is not None:
        return tldr_root
    elif "TLDR_ROOT" in os.environ:
        return Path(os.environ["TLDR_ROOT"])
    raise SystemExit(
        "\x1b[31mPlease set TLDR_ROOT to the location of a clone of https://github.com/tldr-pages/tldr."
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


def get_pages_dir(root: Path):
    return [d for d in root.iterdir() if d.name.startswith("pages")]


def test_get_pages_dir():
    # Create temporary directories with names starting with "pages"

    root = Path("test_root")
    root.mkdir(exist_ok=True)

    # Create temporary directories with names that do not start with "pages"
    (root / "other_dir_1").mkdir()
    (root / "other_dir_2").mkdir()

    # Call the function and verify that it returns an empty list
    result = get_pages_dir(root)
    assert result == []

    (root / "pages_1").mkdir()
    (root / "pages_2").mkdir()
    (root / "other_dir").mkdir()

    # Call the function and verify the result
    result = get_pages_dir(root)
    expected = [root / "pages_1", root / "pages_2"]
    assert result == expected

    for item in root.glob("**/*"):
        item.rmdir()
    root.rmdir()


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
            status_prefix = "\x1b[36m"  # Cyan color
        case "updated":
            status_prefix = "\x1b[34m"  # Blue color
        case _:
            status_prefix = "\x1b[31m"  # Red color (default)

    if dry_run:
        status = f"{type} would be {action}"
    else:
        status = f"{type} {action}"

    return create_colored_line(status_prefix, status)


def test_get_status():
    # Test dry run status
    assert get_status("added", True, "alias") == "\x1b[36malias would be added\x1b[0m"
    assert get_status("updated", True, "link") == "\x1b[34mlink would be updated\x1b[0m"

    # Test non-dry run status
    assert get_status("added", False, "alias") == "\x1b[36malias added\x1b[0m"
    assert get_status("updated", False, "link") == "\x1b[34mlink updated\x1b[0m"

    # Test default color for unknown action
    assert (
        get_status("unknown", True, "alias") == "\x1b[31malias would be unknown\x1b[0m"
    )


def create_colored_line(start_color: str, text: str) -> str:
    """
    Returns:
    str: A colored line
    """

    return f"{start_color}{text}\x1b[0m"


def test_create_colored_line():
    assert create_colored_line("\x1b[36m", "TLDR") == "\x1b[36mTLDR\x1b[0m"
    assert create_colored_line("Hello", "TLDR") == "HelloTLDR\x1b[0m"


def create_argument_parser(description: str) -> argparse.ArgumentParser:
    """
    Create an argument parser that can be extended.
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


def test_create_argument_parser():
    description = "Test argument parser"
    parser = create_argument_parser(description)

    assert isinstance(parser, argparse.ArgumentParser)
    assert parser.description == description

    # Check if each expected argument is added with the correct configurations
    arguments = [
        ("-p", "--page", str, False, ""),
        ("-l", "--language", str, False, ""),
        ("-s", "--stage", None, False, False),
        ("-S", "--sync", None, False, False),
        ("-n", "--dry-run", None, False, False),
    ]
    for short_flag, long_flag, arg_type, is_required, default_value in arguments:
        action = parser._option_string_actions[short_flag]  # Get action for short flag
        assert action.dest.replace("_", "-") == long_flag.lstrip(
            "-"
        )  # Check destination name
        assert action.type == arg_type  # Check argument type
        assert action.required == is_required  # Check if argument is required
        assert action.default == default_value  # Check default value


def stage(paths: list[str], cwd: Path):
    subprocess.call(["git", "add", *paths], cwd=cwd)


@patch("subprocess.call")
def test_stage(mock_subprocess_call):
    paths = ["/path/to/file1", "/path/to/file2"]
    cwd = Path("/path/to/repository")

    # Call the stage function
    stage(paths, cwd)

    # Verify that subprocess.call was called with the correct arguments
    mock_subprocess_call.assert_called_once_with(["git", "add", *paths], cwd=cwd)
