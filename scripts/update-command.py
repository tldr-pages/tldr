#!/usr/bin/env python3
# SPDX-License-Identifier: MIT

"""
A Python script to update the common contents of a command example across all languages.

Usage:
    python3 scripts/update-command.py [-c] [-u] [-n] <PLATFORM> <FILENAME>

Options:
    -c, --common-part COMMON_PART
        Specify the common part to be modified (any content between double brackets will be ignored).
    -u, --updated-common-part UPDATED_COMMON_PART
        Specify the updated common part (any content between double brackets will be ignored).
    -n, --dry-run
        Show what changes would be made without actually modifying the page.


Examples:
    1. Update 'cargo' page interactively:
       python3 scripts/update-command.py common cargo
       Enter the command examples (any content between double curly brackets will be ignored):
       Enter the common part to modify: cargo search {{}}
       Enter the change to be made: cargo search --limit 1 {{}}

    2. Show what changes would be made by updating `sudo apt install {{}}` in 'apt' page to `sudo apt install {{}} --no-confirm`:
       python3 scripts/update-command.py --dry-run -c "sudo apt install {{}}" -u "sudo apt install {{}} --no-confirm" linux apt
"""

from pathlib import Path
import os
import re
import argparse
import sys
from functools import reduce
import logging


class MyFormatter(logging.Formatter):
    grey = "\x1b[0;30m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "%(levelname)s: %(message)s (%(filename)s:%(lineno)d)"

    FORMATS = {
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


logger = logging.getLogger(__name__)
logger.propagate = False

ch = logging.StreamHandler()
ch.setFormatter(MyFormatter())

logger.addHandler(ch)


def get_locales(base_path: Path) -> list[str]:
    return [
        d.name.split(".")[1]
        for d in base_path.iterdir()
        if d.is_dir() and d.name.startswith("pages.")
    ]


def take_cmd_example_with_common_part(cmd_examples: list[str], common_part: str) -> str:
    return next(
        (
            f"`{cmd_example}`"
            for cmd_example in cmd_examples
            if remove_placeholders(cmd_example) == common_part
        ),
        None,
    )


def get_cmd_examples_of_page(page_text: str) -> list[str]:
    command_pattern = re.compile(r"`([^`]+)`")
    return re.findall(command_pattern, page_text)


def find_cmd_example_with_common_part(common_part: str, page_text: str) -> list[str]:
    cmd_examples = get_cmd_examples_of_page(page_text)
    return take_cmd_example_with_common_part(cmd_examples, common_part)


def get_page_path(tldr_root: Path, locale: str, platform: str, filename: str):
    if locale == "":
        return tldr_root / "pages" / platform / filename
    return tldr_root / f"pages.{locale}" / platform / filename


def split_by_curly_brackets(s: str) -> list[str]:
    return re.split(r"(\{\{.*?\}\})", s)


def parse_placeholders(cmd_example: str) -> list[str]:
    return [
        part.strip("{}")
        for part in split_by_curly_brackets(cmd_example)
        if part.startswith("{{") and part.endswith("}}")
    ]


def place_placeholders(cmd_example: str, placeholders: list[str]) -> str:
    return reduce(
        lambda cmd, ph: cmd.replace("{{}}", "{{" + ph + "}}", 1),
        placeholders,
        cmd_example,
    )


def remove_placeholders(cmd_example: str) -> str:
    return re.sub(r"\{\{.*?\}\}", "{{}}", cmd_example)


def add_backticks(cmd_example: str) -> str:
    return "`" + cmd_example.strip("`") + "`"


def update_page(
    page_path: Path,
    old_common_part: str,
    new_common_part: str,
    dry_run: bool,
) -> None:
    with page_path.open("r", encoding="utf-8") as file:
        page_text = file.read()

    logger.info(f"Processing page: {page_path}")

    cmd_example = find_cmd_example_with_common_part(old_common_part, page_text)

    if not cmd_example:
        logger.warning(f"Common part '{old_common_part}' not found in '{page_path}'.")
        return False

    logger.info(f"Found command example: {cmd_example}")
    new_cmd_example = add_backticks(
        place_placeholders(new_common_part, parse_placeholders(cmd_example))
    )
    logger.info(f"{cmd_example} -> {new_cmd_example}")
    if not dry_run:
        new_page_text = page_text.replace(cmd_example, new_cmd_example)

        with page_path.open("w", encoding="utf-8") as file:
            file.write(new_page_text)
    return True


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Update tldr pages.")
    parser.add_argument(
        "platform", help="Relative path to the page from the repository root"
    )
    parser.add_argument("filename", help="Page file name (without .md)")
    parser.add_argument(
        "-c", "--common-part", help="Common part to be modified", required=False
    )
    parser.add_argument(
        "-u", "--updated-common-part", help="Updated common part", required=False
    )
    parser.add_argument(
        "-n",
        "--dry-run",
        action="store_true",
        help="Show what changes would be made without actually modifying the pages",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Increase verbosity level (use -v, -vv)",
    )

    args = parser.parse_args()

    if args.verbose > 0:
        log_levels = [logging.WARNING, logging.INFO]
        log_level = log_levels[min(args.verbose, len(log_levels) - 1)]
    else:
        log_level = logging.ERROR

    logging.basicConfig(level=log_level)

    return args


def update_pages(
    tldr_root: str,
    platform: str,
    filename: str,
    locales: list[str],
    old_common_part: str,
    updated_common_part: str,
    dry_run: bool,
) -> None:
    for locale in locales:
        page_path = get_page_path(tldr_root, locale, platform, filename)
        if page_path.exists() and page_path.is_file():
            exists = update_page(
                page_path,
                old_common_part,
                updated_common_part,
                dry_run,
            )
            if not exists and locale == "":
                logger.warning(
                    f"Common part '{old_common_part}' not found in '{page_path}'."
                )


def clean_cmd_example(cmd_example: str) -> str:
    return remove_placeholders(cmd_example).strip("`")


def get_tldr_root() -> Path:
    f = Path("update-command.py").resolve()
    return next(path for path in f.parents if path.name == "tldr")

    if "TLDR_ROOT" in os.environ:
        return Path(os.environ["TLDR_ROOT"])
    logger.error(
        "Please set TLDR_ROOT to the location of a clone of https://github.com/tldr-pages/tldr."
    )
    sys.exit(1)


def main():
    args = parse_arguments()

    print(
        "Enter the command examples (any content between double curly brackets will be ignored):"
    )
    common_part = (
        args.common_part
        if args.common_part
        else clean_cmd_example(input("Enter the common part to modify: "))
    )
    updated_common_part = (
        args.updated_common_part
        if args.updated_common_part
        else clean_cmd_example(input("Enter the change to be made: "))
    )

    tldr_root = get_tldr_root()
    locales = [""]
    locales.extend(get_locales(tldr_root))

    update_pages(
        tldr_root,
        args.platform,
        args.filename + ".md",
        locales,
        common_part,
        updated_common_part,
        args.dry_run,
    )


if __name__ == "__main__":
    main()
