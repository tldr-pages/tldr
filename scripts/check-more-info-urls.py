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


async def find_all_pages(pages_path: AsyncPath) -> list[AsyncPath]:
    """Find all pages (*.md files) in the specified pages path."""
    pages = []
    async for path_dir in pages_path.glob("*"):
        await aprint(f"  {path_dir.name}: got pages")
        async for page in pages_path.glob("*/*.md"):
            pages.append(page)
    return pages


async def parse_and_make_request(
    page_path: AsyncPath,
    writer: Writer,
    output_file: AsyncPath,
    session: aiohttp.ClientSession,
) -> None:
    """Parse the URL of a single page and write it to the output file if it is bad."""
    async with sem:
        async with page_path.open("r") as page:
            try:
                page_content = await page.read()
            except Exception as exc:
                await aprint(
                    f"{CodeColors.ERROR}Error: {exc}, File: {page.parts[-3:]}{CodeColors.RESET}"
                )
                return

    url = parse_url(page_content)

    if url is not None:
        await make_request_and_write_if_bad(url, writer, output_file, session)


def parse_url(page_content: str) -> list[str]:
    """Parse the URL of '> More information: ' from the page content."""
    return next(
        (
            match.group(1)
            for match in re.finditer(r"> More information: <(.+)>", page_content)
        ),
        None,
    )


async def aprint_colored_status_code_and_url(code: int, url: str) -> None:
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


async def make_request_and_write_if_bad(
    url: str, writer: Writer, output_file: AsyncPath, session: aiohttp.ClientSession
) -> None:
    """Make an HTTP request and write the HTTP status code to the output file if it is bad."""
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
    """Make an HTTP request to a URL and return its status code."""
    async with session.head(url) as response:
        return response.status


async def parse_urls_and_write_if_bad(
    output_file: AsyncPath, pages: list[AsyncPath]
) -> None:
    """Parse all URLs, print their status codes, and write the bad ones to the output file."""
    async with AIOFile(output_file.name, "a") as afp:
        writer = Writer(afp)
        async with aiohttp.ClientSession(
            trust_env=True, timeout=aiohttp.ClientTimeout(total=500)
        ) as session:
            await asyncio.gather(
                *(
                    parse_and_make_request(page_path, writer, output_file, session)
                    for page_path in pages
                )
            )
        await afp.fsync()


async def parse_and_write_bad_urls(
    output_file: AsyncPath, pages_path: str = "./pages"
) -> None:
    """Parse all "More information" URLs, print all, and write the ones with bad status codes (!= 200) to a CSV file."""
    pages_path = AsyncPath(pages_path)
    await aprint("Getting the pages of all platforms...")
    pages = await find_all_pages(pages_path)
    await aprint("Found all pages!")

    await parse_urls_and_write_if_bad(output_file, pages)


async def main() -> None:
    await parse_and_write_bad_urls(AsyncPath("bad-urls.csv"))


if __name__ == "__main__":
    asyncio.run(main())
