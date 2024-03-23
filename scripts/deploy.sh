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

  export SITE_HOME="$HOME/site"
  export LANG_ARCHIVES="$GITHUB_WORKSPACE/language_archives"
  export PDFS="$GITHUB_WORKSPACE/scripts/pdf"
  export INDEX="$GITHUB_WORKSPACE/index.json"
  RELEASE_TAG="$(git describe --tags --abbrev=0)"
  export RELEASE_TAG

  # Configure git.
  git config --global user.email "tldrbotgithub@gmail.com"
  git config --global user.name "tldr bot"
  git config --global push.default simple
  git config --global diff.zip.textconv "unzip -c -a"

  # Decrypt and add deploy key.
  eval "$(ssh-agent -s)"
  echo "$DEPLOY_KEY" > id_ed25519
  chmod 600 id_ed25519
  ssh-add id_ed25519
}

function upload_assets {
  git clone --quiet --depth 1 "git@github.com:tldr-pages/tldr-pages.github.io.git" "$SITE_HOME"

  cp -f "$TLDR_ARCHIVE" "$SITE_HOME/assets/"
  find "$LANG_ARCHIVES" -maxdepth 1 -name "*.zip" -exec cp -f {} "$SITE_HOME/assets/" \;
  cp -f "$INDEX" "$SITE_HOME/assets/"
  find "$PDFS" -maxdepth 1 -name "*.pdf" -exec cp -f {} "$SITE_HOME/assets/" \;

  cd "$SITE_HOME/assets"
  sha256sum -- index.json *.zip > tldr.sha256sums

  # Old way of distributing assets. This needs to be deleted later.
  git add -A
  git commit -m "[GitHub Actions] uploaded assets after commit tldr-pages/tldr@$GITHUB_SHA"
  git push -q
  echo "Assets (pages archive, index and checksums) deployed to the static site."

  gh release --repo tldr-pages/tldr upload --clobber "$RELEASE_TAG" -- \
    tldr.sha256sums \
    "$TLDR_ARCHIVE" \
    "$INDEX" \
    "$LANG_ARCHIVES/"*.zip \
    "$PDFS/"*.pdf
  echo "Assets deployed to GitHub releases."
}

###################################
# MAIN
###################################

initialize
upload_assets
