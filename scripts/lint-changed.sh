#!/bin/bash

MD_FILES=`( git diff --name-only ; git diff --cached --name-only; )\
 | cat | tr " " "\n" | egrep ^.*\.md$`

# Execute Markdown lint if any markdown files have been changed and added to git
[[ -z "$MD_FILES" ]] || GEM_PATH=.gem mdl $MD_FILES
