#!/usr/bin/env bash

# This script is executed by Travis CI when a PR is merged (i.e. in the `deploy` step).
set -ev

function initialize {
  if [ -z "$TLDRHOME" ]; then
    export TLDRHOME=${TRAVIS_BUILD_DIR:-`pwd`}
  fi
  export TLDR_ARCHIVE="tldr.zip"
  export SITE_HOME="$HOME/site"
  export SITE_URL="github.com/tldr-pages/tldr-pages.github.io"
  export SITE_REPO_SLUG="tldr-pages/tldr-pages.github.io"

  # Configure git.
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
  git config --global push.default simple
  git config --global diff.zip.textconv "unzip -c -a"

  # Decrypt and add deploy key.
  eval "$(ssh-agent -s)"
  openssl aes-256-cbc -K $encrypted_973441be79af_key -iv $encrypted_973441be79af_iv -in ./scripts/id_ed25519_tldr_asset_upload.enc -out id_ed25519 -d
  chmod 600 id_ed25519
  ssh-add id_ed25519
}

function rebuild_index {
  npm run build-index
}

function build_archive {
  rm -f $TLDR_ARCHIVE
  cd $TLDRHOME/
  zip -r $TLDR_ARCHIVE pages*/ LICENSE.md
}

function upload_assets {
  git clone --quiet --depth 1 git@github.com:${SITE_REPO_SLUG}.git $SITE_HOME
  mv -f $TLDR_ARCHIVE $SITE_HOME/assets/
  cp -f $TLDRHOME/pages/index.json $SITE_HOME/assets/

  cd $SITE_HOME
  git add -A
  git commit -m "[TravisCI] uploaded assets after commits ${TRAVIS_COMMIT_RANGE}"
  git push -q
}

###################################
# MAIN
###################################

initialize
rebuild_index && echo "Rebuilding index done."
build_archive && echo "Pages archive created."
upload_assets && echo "Assets (pages archive, index) deployed to static site."
