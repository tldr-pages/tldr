#!/usr/bin/env python3
# SPDX-License-Identifier: MIT

"""
A Python script to check for bad (HTTP status code different than 200) "More information" URLs across all pages.

These bad codes typically indicate a page not found or a redirection. They are written to bad-urls.csv with their respective URLs.

Usage:
    python3 scripts/check-more-info-urls.py
"""

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


async def find_md_files(pages_path: AsyncPath) -> list[AsyncPath]:
    """Find all .md files in the specified pages path."""
    md_files = []
    async for path_dir in pages_path.glob("*"):
        await aprint(f"  {path_dir.name}: got pages")
        async for file in pages_path.glob("*/*.md"):
            md_files.append(file)
    return md_files


async def extract_and_check_url(
    file: AsyncPath,
    writer: Writer,
    output_file: AsyncPath,
    session: aiohttp.ClientSession,
) -> None:
    """Extract the URL of a single .md file and check it."""
    async with sem:
        async with file.open("r") as f:
            try:
                content = await f.read()
            except Exception as e:
                await aprint(
                    f"{CodeColors.ERROR}Error: {e}, File: {file.parts[-3:]}{CodeColors.RESET}"
                )
                return

    url = extract_url(content)

    if url is not None:
        await check_url_and_write_if_bad(url, writer, output_file, session)


def extract_url(content: str) -> list[str]:
    """Extract the URL of '> More information: '."""
    return next(
        (
            match.group(1)
            for match in re.finditer(r"> More information: <(.+)>", content)
        ),
        None,
    )


async def aprint_colored_status_code_and_url(code: int, url: str):
    """Print the properly colored status code along with its URL."""
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
    await aprint(f"{color}{code}{CodeColors.RESET} {url}")


async def check_url_and_write_if_bad(
    url: str, writer: Writer, output_file: AsyncPath, session: aiohttp.ClientSession
) -> None:
    """Check URL status and write bad URLs to a file."""
    await aprint(f"??? {url}")
    code = -1
    try:
        code = await get_url_status_code(url, session)
    except aiohttp.ClientError as exc:
        if hasattr(exc, "strerr"):
            await aprint(f"\033[31m{exc.strerr}\033[0m")
        if hasattr(exc, "message"):
            await aprint(f"\033[31m{exc.message}\033[0m")
        else:
            await aprint(f"\033[31m{exc}\033[0m")
    await aprint_colored_status_code_and_url(code, url)

    if code != 200:
        await writer(f'{code},"{url}"\n')


async def get_url_status_code(url: str, session: aiohttp.ClientSession) -> int:
    """Get the status code of a URL."""
    async with session.head(url) as response:
        return response.status


async def find_and_write_bad_urls(
    output_file: AsyncPath, pages_path: str = "./pages"
) -> None:
    """Find and write URLs with bad status codes (!= 200) to a CSV file."""
    pages_path = AsyncPath(pages_path)
    await aprint("Getting the pages of all platforms...")
    md_files = await find_md_files(pages_path)
    await aprint("Found all pages!")

    async with AIOFile(output_file.name, "a") as afp:
        writer = Writer(afp)
        async with aiohttp.ClientSession(
            trust_env=True, timeout=aiohttp.ClientTimeout(total=500)
        ) as session:
            await asyncio.gather(
                *(
                    extract_and_check_url(file, writer, output_file, session)
                    for file in md_files
                )
            )
        await afp.fsync()


async def main():
    await find_and_write_bad_urls(AsyncPath("bad-urls.csv"))


if __name__ == "__main__":
    asyncio.run(main())
