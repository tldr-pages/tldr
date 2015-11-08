#!/bin/bash

MD_FILES=`git diff --cached --name-only | tr " " "\n" | egrep ^.*\.md$`

# Execute Markdown lint if any markdown files have been changed and added to git
