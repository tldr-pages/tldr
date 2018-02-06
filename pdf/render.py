#!/usr/bin/env python3

#A Python script to generate a single PDF document with all the tldr pages. It works by generating 
#intermediate HTML files from existing md files using Python-markdown, applying desired formating 
#through CSS, and finally rendering them as PDF. There is no LaTeX dependency for generating the PDF.

import os
import sys
import glob
import re
import markdown
from weasyprint import HTML

#Unless specified otherwise, this is the default colorscheme
colorscheme = "basic"

oslist = []
allmd = []
group = []
ap = []

#Checking for no path input
try:
    loc = sys.argv[1]
except IndexError:
    print("Please specify a directory and try again!", file = sys.stderr)
    sys.exit(1)

#Checking for invalid path input
if not os.path.isdir(loc):
    print("Invalid directory. Please try again!", file = sys.stderr)
    sys.exit(1)

#Changing colorscheme. Changes are applied only when a valid keyword is received, otherwise
#default colorscheme is maintained
if len(sys.argv) == 3:
    if(sys.argv[2] == "solarized-light" or sys.argv[2] == "solarized-dark"):
        colorscheme = sys.argv[2]

if not loc.endswith('/'):
    loc = loc + "/"

#Writing names of all directories inside 'pages' to a list
for os_dir in os.listdir(loc):
    oslist.append(os_dir)

oslist.sort()

#Required strings to create intermediate HTML files
header = "<html><head><link rel=\"stylesheet\" type=\"text/css\" href=\"" + colorscheme + ".css\"></head><body>\n"
footer = "</body></html>"
title_content = "<h1 class=\"titlemain\">tldr pages</h1><h4 class=\"titlesub\">Simplified and community driven man pages</h4></body></html>"

#Creating title page
with open("title.html", 'w') as f:
    f.write(header + title_content)

group.append(HTML('title.html').render())

for operating_sys in oslist:

    i = 1

    #Required string to create directory title pages
    dir_title = "<h2 class=\"titledir\">" + operating_sys.capitalize() + "</h2></body></html>"

    #Creating directory title page for current directory
    with open("dir_title.html", 'w') as os_html:
        os_html.write(header + dir_title)
    
    group.append(HTML('dir_title.html').render())

    #Creating a list of all md files in the current directory
    for temp in glob.glob(os.path.join(loc + operating_sys, '*.md')):
        allmd.append(temp)

    #Sorting all filenames in the directory, to maintain the order of the PDF
    allmd.sort()

    #Conversion of md to HTML
    for md in allmd:

        output_file = open("htmlout.html", "a")

        with open(md, "r") as inp:
            text = inp.readlines()

        purge = open("htmlout.html", "w")
        purge.close()

        with open("htmlout.html", "a") as out:
            out.write(header)

            for line in text:
                if re.match(r'^>', line):
                    line = line[:0] + '####' + line[1:]

                html = markdown.markdown(line)
                out.write(html)

            out.write(footer)

        group.append(HTML('htmlout.html').render())
        print("Rendered page " + str(i) + " of the directory " + operating_sys)
        i += 1
    
    allmd.clear()

#Merging all the documents into a single PDF
for doc in group:
    for p in doc.pages:
        ap.append(p)

#Writing the PDF to disk, preserving metadata of first tldr page
group[2].copy(ap).write_pdf('tldr.pdf')

if os.path.exists("tldr.pdf"):
    print("\nCreated \'tldr.pdf\' in the current directory!\n")

#Removing unnecessary intermediate files
try:
    os.remove("htmlout.html")
    os.remove("title.html")
    os.remove("dir_title.html")
except OSError:
    pass