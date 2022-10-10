#!/usr/bin/env python3
# SPDX-License-Identifier: MIT

"""
A Python script to generate a single PDF document with all the `tldr` pages. It works by generating
intermediate HTML files from existing md files using Python-markdown, applying desired formatting
through CSS, and finally rendering them as PDF. There is no LaTeX dependency for generating the PDF.
"""

import os
import sys
import glob
import markdown
import argparse
from datetime import datetime

from weasyprint import HTML


def main(loc, colorscheme):

    # Checking correctness of path
    if not os.path.isdir(loc):
        print("Invalid directory. Please try again!", file=sys.stderr)
        sys.exit(1)

    # Set up css style sheets
    csslist = ["basic.css"]
    if colorscheme != "basic":
        csslist.append(colorscheme + ".css")

    # A string that stores all pages in HTML format
    html = (
        '<!doctype html><html><head><meta charset="utf-8"></head>'
        + "<body><h1 class=title-main>tldr pages</h1>"
        + "<div class=title-sub>Simplified and community-driven man pages</div>"
        + "<div class=title-sub><em><small>Generated on "
        + datetime.now().strftime("%c")
        + "</small></em></div>"
        + '<p style="page-break-before: always" ></p>'
    )

    # Writing names of all directories inside 'pages' to a list
    for operating_sys in sorted(os.listdir(loc)):

        # Required string to create directory title pages
        html += (
            "<h1 class=title-dir>"
            + operating_sys.capitalize()
            + "</h1>"
            + '<p style="page-break-before: always" ></p>'
        )

        # Conversion of Markdown to HTML string
        for page_number, md in enumerate(
            sorted(glob.glob(os.path.join(loc, operating_sys, "*.md"))), start=1
        ):
            with open(md, "r") as inp:
                text = inp.readlines()
                # modify our page to have an H2 header, so that it is grouped under
                # the H1 header for the directory
                text[0] = "<h2 class='title-page'>" + text[0][2:] + "</h2>"
                for line in text:
                    if line.startswith(">"):
                        line = "####" + line[1:]
                    html += markdown.markdown(line)
            html += '<p style="page-break-before: always" ></p>'
            print(f"Rendered page {page_number} of the directory {operating_sys}")

    html += "</body></html>"

    # Writing the PDF to disk
    print("\nConverting all pages to PDF...")
    HTML(string=html).write_pdf("tldr-pages.pdf", stylesheets=csslist)

    if os.path.exists("tldr-pages.pdf"):
        print("\nCreated tldr-pages.pdf in the current directory!\n")


if __name__ == "__main__":

    # Parsing the arguments
    parser = argparse.ArgumentParser(
        prog="tldr-pages-to-pdf",
        description="A Python script to generate a single PDF document with all the `tldr` pages.",
    )
    parser.add_argument("dir_path", help="Path to the 'pages' directory")
    parser.add_argument(
        "-c",
        "--color",
        choices=["solarized-light", "solarized-dark", "basic"],
        default="basic",
        help="Color scheme of the PDF",
    )
    args = parser.parse_args()

    main(args.dir_path, args.color)
