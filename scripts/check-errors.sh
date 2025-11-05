#!/bin/bash

grep -r -- "{{\[.*\]}[^}]"
grep -r -- "[^{]{\[.*\]}}"
grep -rE "{{\[[a-z]\|--[a-z]+\]}}"
grep -r "{{-[a-zA-Z][a-zA-Z]|-"
grep -r "{{\[ "
grep -r " ]}}"
find . -type f -print0 | xargs -0 awk '{ q=gsub(/"/,"&"); if(q % 2 != 0) print FILENAME ": " $0 }'
grep -r "{{[^}]*{{"
grep -r www.manned
grep -r linux.org/docs
grep -r linuxcommandlibrary
grep -r /html_node/ | grep -v coreutils | grep -v emacs | grep -v grub
grep -r "#>"
grep -ri "check.* help"
grep -r "?ref_type=heads"
grep -r "?tab=readme-ov-file"
grep -r "?utm_source=chatgpt.com"
grep -r file_path
grep -r http://target
grep -r "directory/}}"
grep -vr "^\`" | grep -i stdin | grep -v "\`stdin\`"
grep -vr "^\`" | grep -i stderr | grep -v "\`stderr\`"
grep -vr "^\`" | grep -i "standard out"
grep -vr "^\`" | grep -i "standard in"
grep -vr "^\`" | grep -i "standard err"
grep -r Generates
grep -r Resolves
grep -r Displays
grep -r Gets
grep -r Restarts
grep -r Executes
grep -r Initializes
grep -r Deploys
grep -r Converts
grep -r Launches
grep -r —
grep -r "’"
grep -r '”'
grep -ir initialise
grep -ir licence
grep -r "^-" | grep "{{"
find . -type f -executable
grep -vr ^\` | grep "'[a-zA-Z][a-zA-Z]*'"
