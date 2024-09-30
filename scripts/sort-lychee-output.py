#!/usr/bin/env python3
# SPDX-License-Identifier: MIT

import re
from pathlib import Path


def extract_failures(markdown_text):
    failure_pattern = re.compile(
        r"^\* \[(\w+)\] \[([^\]]+)\]\([^\)]+\) \| .*$", re.MULTILINE
    )
    return failure_pattern.findall(markdown_text)


def sort_failures_alphabetically(failures):
    return sorted(failures, key=lambda x: x[1])


def format_failures(sorted_failures):
    formatted_failures = []
    for error_info, url in sorted_failures:
        formatted_failures.append(f"* [{error_info}] [{url}]({url})")
    return "\n".join(formatted_failures)


def main():
    input_file = Path("lychee/out.md")

    with input_file.open(encoding="utf-8") as f:
        markdown_text = f.read()

    failures = extract_failures(markdown_text)
    sorted_failures = sort_failures_alphabetically(failures)
    formatted_sorted_failures = format_failures(sorted_failures)

    with input_file.open(mode="w") as f:
        summary_end_index = markdown_text.index("## Errors per input")
        f.write(markdown_text[:summary_end_index])

        f.write("## Errors per input\n\n### Errors in links.txt\n\n")
        f.write(formatted_sorted_failures)
        f.write("\n")


if __name__ == "__main__":
    main()
