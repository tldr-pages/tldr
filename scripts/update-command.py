#!/usr/bin/env python3
# SPDX-License-Identifier: MIT

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


def get_tldr_pages(platform_path: Path) -> list[Path]:
    return [f for f in platform_path.iterdir() if f.is_file() and f.suffix == ".md"]


def take_command_with_common_part(commands: list[str], common_part: str) -> str:
    return next(
        (
            f"`{command}`"
            for command in commands
            if remove_placeholders(command) == common_part
        ),
        None,
    )


def get_commands_of_page(page_text: str) -> list[str]:
    command_pattern = re.compile(r"`([^`]+)`")
    return re.findall(command_pattern, page_text)


def find_command_with_common_part(common_part: str, page_text: str) -> list[str]:
    commands = get_commands_of_page(page_text)
    return take_command_with_common_part(commands, common_part)


def get_page_path(tldr_root: Path, locale: str, platform: str, filename: str):
    if locale == "":
        return tldr_root / "pages" / platform / filename
    return tldr_root / f"pages.{locale}" / platform / filename


def split_by_curly_brackets(s: str) -> list[str]:
    return re.split(r"(\{\{.*?\}\})", s)


def parse_placeholders(command: str) -> list[str]:
    return [
        part.strip("{}")
        for part in split_by_curly_brackets(command)
        if part.startswith("{{") and part.endswith("}}")
    ]


def is_placeholder(s: str) -> bool:
    return s.startswith("{{") and s.endswith("}}")


def place_placeholders(command: str, placeholders: list[str]) -> str:
    return reduce(
        lambda cmd, ph: cmd.replace("{{}}", "{{" + ph + "}}", 1), placeholders, command
    )


def remove_placeholders(command: str) -> str:
    return re.sub(r"\{\{.*?\}\}", "{{}}", command)


def add_backticks(command: str) -> str:
    return "`" + command.strip("`") + "`"


def update_page(
    page_path: Path,
    old_common_part: str,
    new_common_part: str,
    place_placeholders_function,
) -> None:
    with page_path.open("r", encoding="utf-8") as file:
        page_text = file.read()

    logger.info(f"Processing page: {page_path}")

    command = find_command_with_common_part(old_common_part, page_text)

    if not command:
        logger.warning(f"Common part '{old_common_part}' not found in '{page_path}'.")
        return

    logger.info(f"Found command: {command}")
    new_page_text = page_text.replace(
        command,
        add_backticks(
            place_placeholders_function(new_common_part, parse_placeholders(command))
        ),
    )

    with page_path.open("w", encoding="utf-8") as file:
        file.write(new_page_text)


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Update tldr pages.")
    parser.add_argument(
        "platform", help="Relative path to the page from the repository root"
    )
    parser.add_argument("filename", help="Page file name (with .md extension)")
    parser.add_argument(
        "-c", "--common-part", help="Common part to be modified", required=False
    )
    parser.add_argument(
        "-n", "--new-common-part", help="Common part to be modified", required=False
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
    common_part: str,
    new_common_part: str,
) -> None:
    for locale in locales:
        page_path = get_page_path(tldr_root, locale, platform, filename)
        if page_path.exists() and page_path.is_file():
            update_page(page_path, common_part, new_common_part, place_placeholders)


def clean_command(command: str) -> str:
    return remove_placeholders(command).strip("`")


def get_tldr_root() -> Path:
    # if this script is running from tldr/scripts, the parent's parent is the root
    f = Path("update-command.py").resolve()
    if (f.parents[1].name, f.parents[0].name) == ("tldr", "scripts"):
        return f.parents[1]

    if "TLDR_ROOT" in os.environ:
        return Path(os.environ["TLDR_ROOT"])
    logger.error(
        "Please set TLDR_ROOT to the location of a clone of https://github.com/tldr-pages/tldr."
    )
    sys.exit(1)


def main():
    args = parse_arguments()

    print(
        "Enter the commands (any content between double curly brackets will be ignored):"
    )
    common_part = (
        args.common_part
        if args.common_part
        else clean_command(input("Enter the common part to modify: "))
    )
    new_common_part = (
        args.new_common_part
        if args.new_common_part
        else clean_command(input("Enter the change to be made: "))
    )

    tldr_root = get_tldr_root()
    locales = [""]
    locales.extend(get_locales(tldr_root))

    update_pages(
        tldr_root, args.platform, args.filename, locales, common_part, new_common_part
    )


if __name__ == "__main__":
    main()
