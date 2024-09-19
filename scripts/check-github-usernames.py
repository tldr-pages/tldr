#!/usr/bin/env python3
# SPDX-License-Identifier: MIT

"""
A Python script to check if GitHub usernames in .github/CODEOWNERS and MAINTAINERS.md exist.

These usernames are checked against the GitHub API. Non-existent usernames are written to bad-usernames.csv.

Usage:
    python3 scripts/check-github-usernames.py
"""

import os
import re
import asyncio
import aiohttp.client_exceptions
from aioconsole import aprint
from aiofile import AIOFile, Writer
from aiopath import AsyncPath

MAX_CONCURRENCY = 500

sem = asyncio.Semaphore(MAX_CONCURRENCY)


class CodeColors:
    OK = "\033[92m"  # green
    WARNING = "\033[93m"  # yellow
    ERROR = "\033[91m"  # red
    TOO_MANY_REQUESTS = "\033[35m"  # bold
    UNKNOWN = "\033[4m"  # underline
    RESET = "\033[0m"  # reset to no formatting


async def parse_and_make_request(
    file_path: AsyncPath,
    writer: Writer,
    session: aiohttp.ClientSession,
) -> None:
    """Parse the usernames from a single file and write them to the output file if they do not exist."""
    async with sem:
        async with file_path.open("r") as file:
            try:
                file_content = await file.read()
            except Exception as exc:
                await aprint(
                    f"{CodeColors.ERROR}Error: {exc}, File: {file}{CodeColors.RESET}"
                )
                return

    regex = r"\*\*@(\w+)\*\*" if file_path.name == "CODEOWNERS" else r"@(\w+)"

    usernames = extract_usernames(file_content, regex)

    for username in usernames:
        await make_request_and_write_if_bad(username, writer, session)


def extract_usernames(content: str, regex: str) -> list[str]:
    """Extract GitHub usernames from the file content."""
    return re.findall(regex, content)


async def aprint_colored_status_code_and_username(code: int, username: str) -> None:
    """Print the properly colored status code along with its username."""
    color = CodeColors.RESET
    match code:
        case 200:
            color = CodeColors.OK
        case 404:
            color = CodeColors.ERROR
        case 301:
            color = CodeColors.WARNING
        case 301 | 429 | 504 | -1:
            color = CodeColors.TOO_MANY_REQUESTS
        case _:
            color = CodeColors.UNKNOWN
    await aprint(f"{color}{code}{CodeColors.RESET} {username}")


async def make_request_and_write_if_bad(
    username: str, writer: Writer, session: aiohttp.ClientSession
) -> None:
    """Make an HTTP request and write the HTTP status code to the output file if it is bad."""
    await aprint(f"??? {username}")
    code = -1
    try:
        code = await get_username_status_code(username, session)
    except aiohttp.ClientError as exc:
        if hasattr(exc, "strerr"):
            await aprint(f"\033[31m{exc.strerr}\033[0m")
        if hasattr(exc, "message"):
            await aprint(f"\033[31m{exc.message}\033[0m")
        else:
            await aprint(f"\033[31m{exc}\033[0m")
    await aprint_colored_status_code_and_username(code, username)

    if code != 200:
        await writer(f"{code},{username}\n")


async def get_username_status_code(
    username: str, session: aiohttp.ClientSession
) -> int:
    """Make an HTTP request to a URL and return its status code."""
    url = f"https://api.github.com/users/{username}"
    headers = {
        "Authorization": f"token {os.environ.get('GITHUB_TOKEN')}",
    }
    async with session.get(url, headers=headers) as response:
        return response.status


async def parse_usernames_and_write_if_bad(output_file: AsyncPath) -> None:
    """Parse all usernames from .github/CODEOWNERS and MAINTAINERS.md and write the ones that do not exist to a CSV file."""
    files = [AsyncPath(".github/CODEOWNERS"), AsyncPath("MAINTAINERS.md")]

    async with AIOFile(output_file.name, "a") as afp:
        writer = Writer(afp)
        async with aiohttp.ClientSession(
            trust_env=True, timeout=aiohttp.ClientTimeout(total=500)
        ) as session:
            await asyncio.gather(
                *(
                    parse_and_make_request(file_path, writer, session)
                    for file_path in files
                )
            )
        await afp.fsync()


async def main() -> None:
    await parse_usernames_and_write_if_bad(AsyncPath("bad-usernames.csv"))


if __name__ == "__main__":
    asyncio.run(main())
