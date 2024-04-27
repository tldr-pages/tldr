#!/usr/bin/env python3
# SPDX-License-Identifier: MIT

"""
A Python script to check for bad (HTTP status code different than 200) "More information" URLs accross all pages.

These bad codes tipically indicate a not found page or a redirection. They are written to bad-urls.txt with their respective URLs.

Usage:
    python3 scripts/check-more-info-urls.py
"""

import random
import re
import asyncio
import sys
from aiofile import AIOFile, Reader, Writer
import aiohttp.client_exceptions
from aioconsole import aprint
from aiofile import async_open
from aiopath import AsyncPath

MAX_CONCURRENCY = 500

sem = asyncio.Semaphore(MAX_CONCURRENCY)


async def find_md_files(search_path: AsyncPath) -> list[AsyncPath]:
    """Find all .md files in the specified search path."""
    md_files = set()
    async for path_dir in search_path.glob("*"):
        await aprint(path_dir.name)
        async for file in search_path.glob("*/*.md"):
            md_files.add(file)
    return md_files


async def append_if_is_file(path_list: list[AsyncPath], path: AsyncPath):
    """Append the file to the list if it exists"""
    if await path.is_file():
        path_list.add(path)


async def filter_files(md_files: list[AsyncPath]) -> list[AsyncPath]:
    """Filter out non-file paths from the list."""
    filtered_files = set()
    await asyncio.gather(
        *(append_if_is_file(filtered_files, path) for path in md_files)
    )
    return filtered_files


async def process_file(
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
                await aprint(file.parts[-3:])
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


async def check_url_and_write_if_bad(
    url: str, writer: Writer, output_file: AsyncPath, session: aiohttp.ClientSession
) -> None:
    """Check URL status and write bad URLs to a file."""
    await aprint(f"??? {url}")
    code = -1
    try:
        code = await check_url(url, session)
    except aiohttp.ClientError as exc:
        if hasattr(exc, "strerr"):
            await aprint(f"\033[31m{exc.strerr}\033[0m")
        if hasattr(exc, "message"):
            await aprint(f"\033[31m{exc.message}\033[0m")
        else:
            await aprint(f"\033[31m{exc}\033[0m")
    await aprint(f"{code} {url}")

    if 200 > code or code >= 400:
        await writer(f"{code}|{url}\n")


async def check_url(url: str, session: aiohttp.ClientSession) -> int:
    """Get the status code of a URL."""
    async with session.head(url) as response:
        return response.status


async def find_and_write_bad_urls(
    output_file: AsyncPath, search_path: str = "."
) -> None:
    """Find and write bad URLs to a specified file."""
    search_path = AsyncPath(search_path)
    await aprint("Getting pages...")
    md_files = await filter_files(await find_md_files(search_path))
    await aprint("Found all pages!")

    async with AIOFile(output_file.name, "a") as afp:
        writer = Writer(afp)
        async with aiohttp.ClientSession(
            trust_env=True, timeout=aiohttp.ClientTimeout(total=500)
        ) as session:
            await asyncio.gather(
                *(process_file(file, writer, output_file, session) for file in md_files)
            )
        await afp.fsync()


async def main():
    await find_and_write_bad_urls(AsyncPath("bad-urls.txt"), search_path="./pages")


if __name__ == "__main__":
    asyncio.run(main())
