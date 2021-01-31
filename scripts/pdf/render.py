#!/usr/bin/env python3

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

from weasyprint import HTML


def main(loc, colorscheme):

    oslist = []
    allmd = []
    group = []
    ap = []

    # Checking correctness of path
    if not os.path.isdir(loc):
        print("Invalid directory. Please try again!", file=sys.stderr)
        sys.exit(1)

    # Writing names of all directories inside 'pages' to a list
    for os_dir in os.listdir(loc):
        oslist.append(os_dir)

    oslist.sort()

    # Required strings to create intermediate HTML files
    header = '<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="basic.css">'
    if colorscheme != "basic":
        header += '<link rel="stylesheet" href="' + colorscheme + '.css"></head><body>\n'

    header += "</head><body>\n"
    footer = "</body></html>"
    title_content = "<h1 class=title-main>tldr pages</h1>" \
        + "<h4 class=title-sub>Simplified and community-driven man pages</h4>" \
        + "<h6 class=title-sub><em><small>Generated on " + datetime.now().strftime("%c") + "</small></em></h6>" \
        + "</body></html>"

    # Creating title page
    with open("title.html", "w") as f:
        f.write(header + title_content)

    group.append(HTML("title.html").render())

    for operating_sys in oslist:

        # Required string to create directory title pages
        dir_title = "<h2 class=title-dir>" + \
            operating_sys.capitalize() + "</h2></body></html>"

        # Creating directory title page for current directory
        with open("dir_title.html", "w") as os_html:
            os_html.write(header + dir_title)

        group.append(HTML("dir_title.html").render())

        # Creating a list of all md files in the current directory
        for temp in glob.glob(os.path.join(loc, operating_sys, "*.md")):
            allmd.append(temp)

        # Sorting all filenames in the directory, to maintain the order of the PDF
        allmd.sort()

        # Conversion of Markdown to HTML
        for page_number, md in enumerate(allmd, start=1):

                with open(md, "r") as inp:
                    text = inp.readlines()

                with open("htmlout.html", "w") as out:
                    out.write(header)

                    for line in text:
                        if re.match(r'^>', line):
                            line = line[:0] + '####' + line[1:]
                        html = markdown.markdown(line)
                        out.write(html)
                    out.write(footer)

                group.append(HTML("htmlout.html").render())
                print("Rendered page {} of the directory {}".format(
                    str(page_number), operating_sys))

        allmd.clear()

    # Merging all the documents into a single PDF
    for doc in group:
        for p in doc.pages:
            ap.append(p)

    # Writing the PDF to disk, preserving metadata of first `tldr` page
    group[2].copy(ap).write_pdf('tldr-pages.pdf')

    if os.path.exists("tldr-pages.pdf"):
        print("\nCreated tldr-pages.pdf in the current directory!\n")

    # Removing unnecessary intermediate files
    try:
        os.remove("htmlout.html")
        os.remove("title.html")
        os.remove("dir_title.html")
    except OSError:
        print("Error removing temporary file(s)")


if __name__ == "__main__":

    # Parsing the arguments
    parser = argparse.ArgumentParser(prog="tldr-pages-to-pdf", description="A Python script to generate a single PDF document with all the `tldr` pages.")
    parser.add_argument("dir_path", help = "Path to the 'pages' directory")
    parser.add_argument("-c", "--color", choices=["solarized-light", "solarized-dark", "basic"], default="basic", help="Color scheme of the PDF")
    args = parser.parse_args()

    main(args.dir_path, args.color)
