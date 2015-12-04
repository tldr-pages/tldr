#!/usr/bin/env bash

set -ev

function initialize {
  if [ -z "$TLDRHOME" ]; then
    export TLDRHOME=${TRAVIS_BUILD_DIR:-`pwd`}
  fi
  export TLDR_ARCHIVE="tldr.zip"
  export SITE_HOME="$HOME/site"
  export SITE_URL="github.com/tldr-pages/tldr-pages.github.io"

  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
  git config --global push.default simple
  git config --global diff.zip.textconv "unzip -c -a"
}

function rebuild_index {
  $TLDRHOME/scripts/build_index.rb
  echo "Rebuilding index is done"
}

function build_archive {
  echo "Removing $TLDR_ARCHIVE if it exists"
  rm -f $TLDR_ARCHIVE

  echo "Creating an archive $TLDR_ARCHIVE"
  cd $TLDRHOME/
  zip -r $TLDR_ARCHIVE pages/ LICENSE.md
}

function upload_assets {
  echo "Uploading assets to static site"

  git clone --quiet --depth 1 https://${GH_TOKEN}@${SITE_URL} $SITE_HOME
  mv -f $TLDR_ARCHIVE $SITE_HOME/assets/
  cp -f $TLDRHOME/pages/index.json $SITE_HOME/assets/

  cd $SITE_HOME
  git add -A .
  git commit -m "[TravisCI] uploaded assets after commits ${TRAVIS_COMMIT_RANGE}"
  if [[ ! `git push -q` ]]; then
    echo "Cannot push to a static site"
  else
    echo "Assets deployed"
  fi
}

###################################
# MAIN
###################################

if [ ! "$TRAVIS_PULL_REQUEST" == "false" ]; then
  echo "This is a Pull Request, no index rebuild needed"
elif [ ! "$TRAVIS_BRANCH" == "master" ]; then
  echo "This is not a master branch, no index rebuild needed"
else
  initialize
  rebuild_index
  build_archive
  upload_assets
fi
