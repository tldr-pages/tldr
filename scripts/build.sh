#!/usr/bin/env bash

# This script is executed by Travis CI for every successful push (on any branch, PR or not).
set -ex

function initialize {
  if [ -z "$TLDRHOME" ]; then
    export TLDRHOME=${TRAVIS_BUILD_DIR:-$(pwd)}
  fi

  export TLDR_ARCHIVE="tldr.zip"
}

function build_index {
  npm run build-index
  cp index.json pages/
  echo "Pages index succesfully built."
}

function build_archive {
  rm -f "$TLDR_ARCHIVE"
  cd "$TLDRHOME/"
  zip -q -r "$TLDR_ARCHIVE" pages* LICENSE.md index.json
  echo "Pages archive succesfully built."
}

###################################
# MAIN
###################################

initialize
build_index
build_archive
