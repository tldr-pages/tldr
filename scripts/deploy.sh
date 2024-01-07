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

  if [[ -z $TLDRHOME ]]; then
    export TLDRHOME=${GITHUB_WORKSPACE:-$(pwd)}
  fi

  export SITE_HOME="$HOME/site"

  # Configure git.
  git config --global user.email "tldrbotgithub@gmail.com"
  git config --global user.name "tldr bot"
  git config --global push.default simple
  git config --global diff.zip.textconv "unzip -c -a"

  # Decrypt and add deploy key.
  eval "$(ssh-agent -s)"
  echo "$DEPLOY_KEY"> id_ed25519
  chmod 600 id_ed25519
  ssh-add id_ed25519
}

function upload_assets {
  git clone --quiet --depth 1 "git@github.com:tldr-pages/tldr-pages.github.io.git" "$SITE_HOME"

  mv -f "$TLDR_ARCHIVE" "$SITE_HOME/assets/"
  find "$TLDRHOME/language_archives" -maxdepth 1 -name '*.zip' -exec mv -f {} "$SITE_HOME/assets/" \;
  cp -f "$TLDRHOME/index.json" "$SITE_HOME/assets/"
  find "$TLDRHOME/scripts/pdf" -maxdepth 1 -name '*.pdf' -exec mv -f {} "$SITE_HOME/assets/" \;

  cd "$SITE_HOME/assets"
  sha256sum -- index.json *.zip > tldr.sha256sums

  git add -A
  git commit -m "[GitHub Actions] uploaded assets after commit tldr-pages/tldr@$GITHUB_SHA"
  git push -q
  echo "Assets (pages archive, index and checksums) deployed to the static site."
}

###################################
# MAIN
###################################

initialize
upload_assets
