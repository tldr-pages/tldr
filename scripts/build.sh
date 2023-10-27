#!/usr/bin/env bash
# SPDX-License-Identifier: MIT

# This script is executed by GitHub Actions for every successful push (on any branch, PR or not).
set -ex

function initialize {
  if [[ -z $TLDRHOME ]]; then
    export TLDRHOME=${GITHUB_WORKSPACE:-$(pwd)}
  fi

  if [[ -z $TLDR_LANG_ARCHIVES_DIRECTORY ]]; then
    export TLDR_LANG_ARCHIVES_DIRECTORY="${GITHUB_WORKSPACE:-$(pwd)}/language_archives"
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

function build_translation_archives {
  local source_directory="$TLDRHOME"
  local target_directory="$TLDR_LANG_ARCHIVES_DIRECTORY"
  mkdir -p "$target_directory"
  rm -f "$target_directory"/*

  for lang_dir in "$source_directory"/pages*; do
    # Skip symlinks (pages.en) and things that are not directories
    if [[ ! -d $lang_dir || -h $lang_dir ]]; then
      continue
    fi

    local lang=$(basename "$lang_dir")
    local archive_name="tldr-$lang.zip"

    # Create the zip archive

    cd "$lang_dir"
    zip -q -r "$target_directory/$archive_name" .
    zip -q -j "$target_directory/$archive_name" "$source_directory/LICENSE.md"

    echo "Pages archive of $archive_name successfully created."
  done

  cd "$target_directory"
  cp tldr-pages.zip tldr-pages.en.zip
}

###################################
# MAIN
###################################

initialize
build_index
build_archive
build_translation_archives
