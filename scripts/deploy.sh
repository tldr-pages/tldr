#!/usr/bin/env bash
# SPDX-License-Identifier: MIT

# This script is executed by GitHub Actions when a PR is merged (i.e. in the `deploy` step).
set -ex

function initialize {
  export TLDR_ARCHIVE="tldr.zip"

  if [[ ! -f $TLDR_ARCHIVE ]]; then
    echo "No changes to deploy."
    exit 0
  fi

  export ASSETS="$HOME/assets"
  export LANG_ARCHIVES="$GITHUB_WORKSPACE/language_archives"
  export PDFS="$GITHUB_WORKSPACE/scripts/pdf"
  export INDEX="$GITHUB_WORKSPACE/index.json"
  RELEASE_TAG="$(git describe --tags --abbrev=0)"
  export RELEASE_TAG
}

function upload_assets {
  mkdir "$ASSETS"

  # Assets are built only for changed directories.
  # We need the old zip archives to update `tldr.sha256sums`.
  gh release --repo tldr-pages/tldr download "$RELEASE_TAG" --dir "$ASSETS" --pattern "*.zip"

  # Suppress errors from unmatched patterns if some files don't exist.
  shopt -s nullglob
  cp -t "$ASSETS" "$TLDR_ARCHIVE" "$INDEX" "$LANG_ARCHIVES"/*.zip "$PDFS"/*.pdf

  cd "$ASSETS"
  sha256sum -- index.json *.zip > tldr.sha256sums

  gh release --repo tldr-pages/tldr upload --clobber "$RELEASE_TAG" -- \
    tldr.sha256sums \
    "$TLDR_ARCHIVE" \
    "$INDEX" \
    "$LANG_ARCHIVES/"*.zip \
    "$PDFS/"*.pdf

  shopt -u nullglob
  echo "Assets deployed to GitHub releases."
}

###################################
# MAIN
###################################

initialize
upload_assets
