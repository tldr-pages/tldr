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
import re
import markdown
import argparse
from datetime import datetime

from weasyprint import HTML, CSS

def main(loc, colorscheme):
    oslist = []
    allmd = []

    # Checking correctness of path
    if not os.path.isdir(loc):
        print("Invalid directory. Please try again!", file=sys.stderr)
        sys.exit(1)

    # Writing names of all directories inside 'pages' to a list
    for os_dir in os.listdir(loc):
        oslist.append(os_dir)
    oslist.sort()

    # A string that stores pages in HTML format
    html = ''

    # Set up css style sheets
    csslist = [CSS("basic.css")]
    if colorscheme != "basic":
        csslist.append(CSS(colorscheme + ".css"))

    # Required strings to create intermediate HTML files
    html += '<!doctype html><html><head><meta charset="utf-8">' \
        +"</head><body><h1 class=title-main>tldr pages</h1>" \
        + "<h4 class=title-sub>Simplified and community-driven man pages</h4>" \
        + "<h6 class=title-sub><em><small>Generated on " + datetime.now().strftime("%c") + "</small></em></h6>" \
        + '<p style="page-break-before: always" ></p>'

    for operating_sys in oslist:
        # Required string to create directory title pages
        html += "<h2 class=title-dir>" + operating_sys.capitalize() + "</h2>" \
            + '<p style="page-break-before: always" ></p>'

        # Creating a list of all md files in the current directory
        for temp in glob.glob(os.path.join(loc, operating_sys, "*.md")):
            allmd.append(temp)

        # Sorting all filenames in the directory, to maintain the order of the PDF
        allmd.sort()

        # Conversion of Markdown to HTML string
        for page_number, md in enumerate(allmd, start=1):
            with open(md, "r") as inp:
                text = inp.readlines()
                for line in text:
                    if re.match(r'^>', line):
                        line = line[:0] + '####' + line[1:]
                    html += markdown.markdown(line)
            html += '<p style="page-break-before: always" ></p>'
            print("Rendered page {} of the directory {}".format(
                str(page_number), operating_sys))

        allmd.clear()
    
    # Writing the PDF to disk
    html += "</body></html>"
    HTML(string=html).write_pdf("tldr-page.pdf", stylesheets=csslist)

    if os.path.exists("tldr-pages.pdf"):
        print("\nCreated tldr-pages.pdf in the current directory!\n")

if __name__ == "__main__":

    # Parsing the arguments
    parser = argparse.ArgumentParser(prog="tldr-pages-to-pdf", description="A Python script to generate a single PDF document with all the `tldr` pages.")
    parser.add_argument("dir_path", help = "Path to the 'pages' directory")
    parser.add_argument("-c", "--color", choices=["solarized-light", "solarized-dark", "basic"], default="basic", help="Color scheme of the PDF")
    args = parser.parse_args()

    main(args.dir_path, args.color)
