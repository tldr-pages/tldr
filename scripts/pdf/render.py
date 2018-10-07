#!/usr/bin/env python3

#A Python script to generate a single PDF document with all the tldr pages. It works by generating 
#intermediate HTML files from existing md files using Python-markdown, applying desired formatting 
#through CSS, and finally rendering them as PDF. There is no LaTeX dependency for generating the PDF.

import os
import sys
import glob
import re
import markdown
import argparse

from weasyprint import HTML

def main(loc, colorscheme):

    oslist = []
    allmd = []
    group = []
    ap = []

    #Checking correctness of path
    if not os.path.isdir(loc):
        print("Invalid directory. Please try again!", file = sys.stderr)
        sys.exit(1)

    #Writing names of all directories inside 'pages' to a list
    for os_dir in os.listdir(loc):
        oslist.append(os_dir)

    oslist.sort()

    #Required strings to create intermediate HTML files
    header = "<html><head><link rel=stylesheet type=text/css href=" + colorscheme + ".css></head><body>\n"
    footer = "</body></html>"
    title_content = "<h1 class=titlemain>tldr pages</h1><h4 class=titlesub>Simplified and community driven man pages</h4></body></html>"

    #Creating title page
    with open("title.html", 'w') as f:
        f.write(header + title_content)

    group.append(HTML('title.html').render())

    for operating_sys in oslist:

        i = 1

        #Required string to create directory title pages
        dir_title = "<h2 class=titledir>" + operating_sys.capitalize() + "</h2></body></html>"

        #Creating directory title page for current directory
        with open("dir_title.html", 'w') as os_html:
            os_html.write(header + dir_title)
        
        group.append(HTML('dir_title.html').render())

        #Creating a list of all md files in the current directory
        for temp in glob.glob(os.path.join(loc, operating_sys, '*.md')):
            allmd.append(temp)

        #Sorting all filenames in the directory, to maintain the order of the PDF
        allmd.sort()

        #Conversion of md to HTML
        for md in allmd:

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

            group.append(HTML('htmlout.html').render())
            print("Rendered page {} of the directory {}".format(str(i), operating_sys))
            i += 1
        
        allmd.clear()

    #Merging all the documents into a single PDF
    for doc in group:
        for p in doc.pages:
            ap.append(p)

    #Writing the PDF to disk, preserving metadata of first tldr page
    group[2].copy(ap).write_pdf('tldr.pdf')

    if os.path.exists("tldr.pdf"):
        print("\nCreated tldr.pdf in the current directory!\n")

    #Removing unnecessary intermediate files
    try:
        os.remove("htmlout.html")
        os.remove("title.html")
        os.remove("dir_title.html")
    except OSError:
        print("Error removing temporary file(s)")


if __name__ == '__main__':

    #Unless specified otherwise by the user, this is the default colorscheme
    colorscheme = "basic"

    #Parsing the arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("dir_path", help = "Path to tldr 'pages' directory")
    parser.add_argument("-c", choices=["solarized-light", "solarized-dark"], help="Color scheme of the PDF")
    args = parser.parse_args()
    
    loc = args.dir_path
    if args.c == "solarized-light" or args.c == "solarized-dark":
        colorscheme = args.c
        
    main(loc, colorscheme)
