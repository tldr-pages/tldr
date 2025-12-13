#!/bin/bash

grep -r -- "{{\[[^}]*\]}[^}]"
grep -r -- "[^{]{\[.*\]}}"
grep -rE "{{\[[a-z]\|--[a-z]+\]}}"
grep -r "{{-[a-zA-Z][a-zA-Z]|-"
grep -r "{{\[ "
grep -r " ]}}"
# shellcheck disable=SC2016
find . -type f -print0 | xargs -0 awk '{ q=gsub(/"/,"&"); if(q % 2 != 0) print FILENAME ": " $0 }'
find . -type f -print0 | xargs -0 awk '{ b=gsub(/`/,"&"); if(b % 2 != 0) print FILENAME ": " $0 }'
grep -r "{{[^}]*{{"
grep -r www.manned
grep -r linux.org/docs
grep -r linuxcommandlibrary
grep -r /html_node/| grep -Ev "coreutils|emacs|grub"
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
grep -r Converts
grep -r Deploys
grep -r Displays
grep -r Executes
grep -r Generates
grep -r Gets
grep -r Initializes
grep -r Launches
grep -r Queries
grep -r Resolves
grep -r Restarts
grep -r …
grep -r –
grep -r —
grep -r "’"
grep -r '”'
grep -r \`\`
grep -r $'\u00A0'
grep -r $'\u200A'
grep -r $'\u200B'
grep -r $'\u200C'
grep -r $'\u200D'
grep -r $'\u202F'
grep -r $'\uFEFF'
grep -ir initialise
grep -ir licence
grep -r backtic | grep -v backtick
grep -r "^-" | grep "{{"
find . -type f -executable
grep -vr ^\` | grep "'[a-zA-Z][a-zA-Z]*'"
