#!/usr/bin/env bash
# SPDX-License-Identifier: MIT

# This script is executed by GitHub Actions when a PR is merged (i.e. in the `Build PDF` step).
set -ex

function process_page {
  pageDir="$1"
  folder=$(basename "${pageDir}")
  case $folder in
    pages.bn | pages.ja | pages.ko | pages.ml | pages.ta | pages.th | pages.zh | pages.zh_TW)
      ;;
    pages)
      python3 render.py "${pageDir}" -c solarized-light
      ;;
    *)
      language="${folder##*.}"
      python3 render.py "${pageDir}" -c basic -o "tldr-book-${language}.pdf"
      ;;
  esac
}

function main {
  languageId="$1"
  if [ -z "$languageId" ]; then
    changedFiles=$(git diff-tree --no-commit-id --name-only -r "$(git rev-parse HEAD)")
    changedPageDirs=$(echo "$changedFiles" | awk -F/ '/^(pages[^\/]+|pages)\//{print $1}' | sort -u)
    if [ -z "$changedPageDirs" ]; then
      pageDirs=()
    else
      mapfile -t pageDirs <<< "$changedPageDirs"
    fi
  else
    case $languageId in
      all)
        pageDirs=(../../pages*)
        ;;
      bn | ja | ko | ml | ta | th | zh | zh_TW)
        echo "${languageId} is not supported to build a PDF"
        ;;
      en)
        pageDirs=("pages")
        ;;
      *)
        pageDirs=("pages.${languageId}")
        ;;
    esac
  fi
  
  for pageDir in "${pageDirs[@]}"; do
    process_page "../../${pageDir}"
  done
}

###################################
# MAIN
###################################

main $1
