#A Python script to generate a single PDF document for a specified section of tldr pages. It works by
#generating intermediate HTML files from existing MD files using Python-markdown, applying desired formating 
#through CSS, and finally rendering them as PDF. There is no LaTeX dependency for generating the PDF.

import os
import sys
import glob
import re
import markdown
from weasyprint import HTML

#Unless specified otherwise, this is the default colorscheme
colorscheme = "basic"

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

#Required strings to create intermediate HTML files
header = "<html><head><link rel=\"stylesheet\" type=\"text/css\" href=\"" + colorscheme + ".css\"></head><body>\n"
footer = "</body></html>"
titlecontent = "<h1 class=\"titlea\">tldr pages</h1><h4 class=\"titleb\">Simplified and community driven man pages</h4></body></html>"

for temp in glob.glob(os.path.join(loc, '*.md')):
    allmd.append(temp)

#Sorting all filenames in the directory, to maintain the order of the PDF
allmd.sort()

#Creating title page
with open("title.html", 'w') as f:
    f.write(header + titlecontent)

group.append(HTML('title.html').render())

i=1

#Conversion of MD to HTML
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
    print("Rendered page " + str(i))
    
    i += 1

#Merging all the documents into a single PDF
for doc in group:
    for p in doc.pages:
        ap.append(p)

#Writing the PDF to disk, preserving metadata of first page
group[1].copy(ap).write_pdf('tldr.pdf')

if os.path.exists("tldr.pdf"):
    print("\nCreated a file tldr.pdf in the current directory!\n")

#Removing unnecessary intermediate files
try:
    os.remove("htmlout.html")
    os.remove("title.html")
except OSError:
    pass