#!/usr/bin/env bash
# SPDX-License-Identifier: MIT

# This script is executed by GitHub Actions for every successful push (on any branch, PR or not).
set -ex

function initialize {
  if [ -z "$TLDRHOME" ]; then
    export TLDRHOME=${GITHUB_WORKSPACE:-$(pwd)}
  fi

  export TLDR_ARCHIVE="tldr.zip"
}

function build_index {
  npm run build-index
  echo "Pages index successfully built."
}

function build_archive {
  rm -f "$TLDR_ARCHIVE"
  cd "$TLDRHOME/"
  zip -q -r "$TLDR_ARCHIVE" pages* LICENSE.md index.json
  echo "Pages archive successfully built."
}

###################################
# MAIN
###################################

initialize
build_index
build_archive
