#!/bin/bash

tput setaf 5
echo Placeholders
tput sgr0
grep -r -- "{{\[[^}]*\]}[^}]"
grep -r -- "[^{]{\[.*\]}}"
grep -rE "{{\[[a-z]\|--[a-z]+\]}}"
grep -r "{{-[a-zA-Z][a-zA-Z]|-"
grep -r "{{\[ "
grep -r " ]}}"

tput setaf 5
echo
echo Brackets
tput sgr0
# shellcheck disable=SC2016
find . -type f -print0 | xargs -0 awk '{ q=gsub(/"/,"&"); if(q % 2 != 0) print FILENAME ": " $0 }'
# shellcheck disable=SC2016
find . -type f -print0 | xargs -0 awk '{ b=gsub(/`/,"&"); if(b % 2 != 0) print FILENAME ": " $0 }'
grep -r "{{[^}]*{{"

tput setaf 5
echo
echo Man pages
tput sgr0
grep -r www.manned
grep -r linux.org/docs
grep -r linuxcommandlibrary
grep -r /html_node/| grep -Ev "coreutils|emacs|grub"
grep -r "#>"

tput setaf 5
echo
echo Wrong wording
tput sgr0
grep -ri "check.* help"

tput setaf 5
echo
echo Github and gitlab useless parts
tput sgr0
grep -r "?ref_type=heads"
grep -r "?tab=readme-ov-file"
grep -r "?utm_source=chatgpt.com"

tput setaf 5
echo
echo Wrong filepath or url format
tput sgr0
grep -r file_path
grep -r http://target
grep -r "directory/}}"

tput setaf 5
echo
echo Standard streams
tput sgr0
grep -vr "^\`" | grep -i stdin | grep -v "\`stdin\`"
grep -vr "^\`" | grep -i stderr | grep -v "\`stderr\`"
grep -vr "^\`" | grep -i "standard out"
grep -vr "^\`" | grep -i "standard in"
grep -vr "^\`" | grep -i "standard err"

tput setaf 5
echo
echo Imperative mood
tput sgr0
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

tput setaf 5
echo
echo Character mistakes
tput sgr0
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

tput setaf 5
echo
echo Typos
tput sgr0
grep -ir initialise
grep -ir licence
grep -r backtic | grep -v backtick

tput setaf 5
echo
echo Placeholders in descriptions
tput sgr0
grep -r "^-" | grep "{{"
grep -r "^>" | grep {{

tput setaf 5
echo
echo File contains executable permissions
tput sgr0
find . -type f -executable

tput setaf 5
echo
echo Use of apostrophe instead of backtick
tput sgr0
grep -vr ^\` | grep "'[a-zA-Z][a-zA-Z]*'"
