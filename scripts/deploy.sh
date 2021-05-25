#!/usr/bin/env bash

# This script is executed by GitHub Actions when a PR is merged (i.e. in the `deploy` step).
set -ex

function initialize {
  if [ -z "$TLDRHOME" ]; then
    export TLDRHOME=${GITHUB_WORKSPACE:-$(pwd)}
  fi

  export TLDR_ARCHIVE="tldr.zip"
  export SITE_HOME="$HOME/site"
  export SITE_REPO_SLUG="tldr-pages/tldr-pages.github.io"

  # Configure git.
  git config --global user.email "tldrbotgithub@gmail.com"
  git config --global user.name "tldr bot"
  git config --global push.default simple
  git config --global diff.zip.textconv "unzip -c -a"

  # Decrypt and add deploy key.
  eval "$(ssh-agent -s)"
  echo "${DEPLOY_KEY}"> id_ed25519
  chmod 600 id_ed25519
  ssh-add id_ed25519
}

function upload_assets {
  git clone --quiet --depth 1 git@github.com:${SITE_REPO_SLUG}.git "$SITE_HOME"
  mv -f "$TLDR_ARCHIVE" "$SITE_HOME/assets/"
  cp -f "$TLDRHOME/index.json" "$SITE_HOME/assets/"

  # Copy PDF to assets
  if [[ -f "${TLDRHOME}/scripts/pdf/tldr-pages.pdf" ]]; then
    cp -f "${TLDRHOME}/scripts/pdf/tldr-pages.pdf" "${SITE_HOME}/assets/tldr-book.pdf"
  fi

  cd "$SITE_HOME"
  git add -A
  git commit -m "[GitHub Actions] uploaded assets after commit tldr-pages/tldr@${GITHUB_SHA}"
  git push -q

  echo "Assets (pages archive, index) deployed to static site."
}

###################################
# MAIN
###################################

initialize
upload_assets
