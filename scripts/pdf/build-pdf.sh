#!/usr/bin/env bash
# SPDX-License-Identifier: MIT

# This script is executed by GitHub Actions when a PR is merged (i.e. in the `Build PDF` step).
set -ex

function process_page {
  pageDir="$1"
  folder=$(basename "${pageDir}")
  language="${folder##*.}"
  case $folder in
    pages.bn | pages.ja | pages.ko | pages.ml | pages.ta | pages.th | pages.zh | pages.zh_TW)
      ;;
    pages)
      python3 render.py "${pageDir}" -c solarized-light
      ;;
    *)
      python3 render.py "${pageDir}" -c basic -o "tldr-book-${language}.pdf"
      ;;
  esac
}

function main {
  for pageDir in ../../pages*; do
    process_page "${pageDir}"
  done
}

###################################
# MAIN
###################################

main
