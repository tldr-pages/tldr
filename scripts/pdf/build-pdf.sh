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
  type="$1"
  case $type in
    "all")
      for pageDir in ../../pages*; do
        process_page "${pageDir}"
      done
      ;;
    *)
      changedFiles=$(git diff-tree --no-commit-id --name-only -r "$(git rev-parse HEAD)")
      changedPageDirs=$(echo "$changedFiles" | awk -F/ '/^(pages[^\/]+|pages)\//{print $1}' | sort -u)
      mapfile -t pageDirs <<< "$changedPageDirs"

      for pageDir in "${pageDirs[@]}"; do
          process_page "../../${pageDir}"
      done
      ;;
  esac
}

###################################
# MAIN
###################################

main $1
