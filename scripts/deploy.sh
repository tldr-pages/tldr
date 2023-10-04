#!/usr/bin/env bash
# SPDX-License-Identifier: MIT

# This script is executed by GitHub Actions when a PR is merged (i.e. in the `deploy` step).
set -ex

function initialize {
  if [ -z "$TLDRHOME" ]; then
    export TLDRHOME=${GITHUB_WORKSPACE:-$(pwd)}
  fi

  export TLDR_LANG_ARCHIVES_DIRECTORY="$TLDRHOME/language_archives"
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
  mv -f "${TLDR_LANG_ARCHIVES_DIRECTORY}"/*.zip "$SITE_HOME/assets/"
  rm -rf "$TLDR_LANG_ARCHIVES_DIRECTORY"
  cp -f "$TLDRHOME/index.json" "$SITE_HOME/assets/"
  cp -f "${TLDRHOME}/scripts/pdf/tldr-pages.pdf" "${SITE_HOME}/assets/tldr-book.pdf"
  cp -f "${TLDRHOME}/scripts/pdf/tldr-pages-ar.pdf" "${SITE_HOME}/assets/tldr-book-ar.pdf"
  cp -f "${TLDRHOME}/scripts/pdf/tldr-pages-bn.pdf" "${SITE_HOME}/assets/tldr-book-bn.pdf"
  cp -f "${TLDRHOME}/scripts/pdf/tldr-pages-bs.pdf" "${SITE_HOME}/assets/tldr-book-bs.pdf"
  cp -f "${TLDRHOME}/scripts/pdf/tldr-pages-ca.pdf" "${SITE_HOME}/assets/tldr-book-ca.pdf"
  cp -f "${TLDRHOME}/scripts/pdf/tldr-pages-da.pdf" "${SITE_HOME}/assets/tldr-book-da.pdf"
  cp -f "${TLDRHOME}/scripts/pdf/tldr-pages-de.pdf" "${SITE_HOME}/assets/tldr-book-de.pdf"
  cp -f "${TLDRHOME}/scripts/pdf/tldr-pages-es.pdf" "${SITE_HOME}/assets/tldr-book-es.pdf"
  cp -f "${TLDRHOME}/scripts/pdf/tldr-pages-fa.pdf" "${SITE_HOME}/assets/tldr-book-fa.pdf"
  cp -f "${TLDRHOME}/scripts/pdf/tldr-pages-fr.pdf" "${SITE_HOME}/assets/tldr-book-fr.pdf"
  cp -f "${TLDRHOME}/scripts/pdf/tldr-pages-hi.pdf" "${SITE_HOME}/assets/tldr-book-hi.pdf"
  cp -f "${TLDRHOME}/scripts/pdf/tldr-pages-id.pdf" "${SITE_HOME}/assets/tldr-book-id.pdf"
  cp -f "${TLDRHOME}/scripts/pdf/tldr-pages-it.pdf" "${SITE_HOME}/assets/tldr-book-it.pdf"
  cp -f "${TLDRHOME}/scripts/pdf/tldr-pages-lo.pdf" "${SITE_HOME}/assets/tldr-book-lo.pdf"
  cp -f "${TLDRHOME}/scripts/pdf/tldr-pages-ml.pdf" "${SITE_HOME}/assets/tldr-book-ml.pdf"
  cp -f "${TLDRHOME}/scripts/pdf/tldr-pages-ne.pdf" "${SITE_HOME}/assets/tldr-book-ne.pdf"
  cp -f "${TLDRHOME}/scripts/pdf/tldr-pages-nl.pdf" "${SITE_HOME}/assets/tldr-book-nl.pdf"
  cp -f "${TLDRHOME}/scripts/pdf/tldr-pages-no.pdf" "${SITE_HOME}/assets/tldr-book-no.pdf"
  cp -f "${TLDRHOME}/scripts/pdf/tldr-pages-pl.pdf" "${SITE_HOME}/assets/tldr-book-pl.pdf"
  cp -f "${TLDRHOME}/scripts/pdf/tldr-pages-pt_BR.pdf" "${SITE_HOME}/assets/tldr-book-pt_BR.pdf"
  cp -f "${TLDRHOME}/scripts/pdf/tldr-pages-pt_PT.pdf" "${SITE_HOME}/assets/tldr-book-pt_PT.pdf"
  cp -f "${TLDRHOME}/scripts/pdf/tldr-pages-ro.pdf" "${SITE_HOME}/assets/tldr-book-ro.pdf"
  cp -f "${TLDRHOME}/scripts/pdf/tldr-pages-ru.pdf" "${SITE_HOME}/assets/tldr-book-ru.pdf"
  cp -f "${TLDRHOME}/scripts/pdf/tldr-pages-sh.pdf" "${SITE_HOME}/assets/tldr-book-sh.pdf"
  cp -f "${TLDRHOME}/scripts/pdf/tldr-pages-sr.pdf" "${SITE_HOME}/assets/tldr-book-sr.pdf"
  cp -f "${TLDRHOME}/scripts/pdf/tldr-pages-sv.pdf" "${SITE_HOME}/assets/tldr-book-sv.pdf"
  cp -f "${TLDRHOME}/scripts/pdf/tldr-pages-ta.pdf" "${SITE_HOME}/assets/tldr-book-ta.pdf"
  cp -f "${TLDRHOME}/scripts/pdf/tldr-pages-th.pdf" "${SITE_HOME}/assets/tldr-book-th.pdf"
  cp -f "${TLDRHOME}/scripts/pdf/tldr-pages-tr.pdf" "${SITE_HOME}/assets/tldr-book-tr.pdf"
  cp -f "${TLDRHOME}/scripts/pdf/tldr-pages-uk.pdf" "${SITE_HOME}/assets/tldr-book-uk.pdf"
  cp -f "${TLDRHOME}/scripts/pdf/tldr-pages-uz.pdf" "${SITE_HOME}/assets/tldr-book-uz.pdf"


  sha256sum \
    "${SITE_HOME}/assets/index.json" \
    "${SITE_HOME}/assets/"*.zip \
    "${SITE_HOME}/assets/tldr-book.pdf" \
    "${SITE_HOME}/assets/tldr-book-ar.pdf" \
    "${SITE_HOME}/assets/tldr-book-bn.pdf" \
    "${SITE_HOME}/assets/tldr-book-bs.pdf" \
    "${SITE_HOME}/assets/tldr-book-ca.pdf" \
    "${SITE_HOME}/assets/tldr-book-da.pdf" \
    "${SITE_HOME}/assets/tldr-book-de.pdf" \
    "${SITE_HOME}/assets/tldr-book-es.pdf" \
    "${SITE_HOME}/assets/tldr-book-fa.pdf" \
    "${SITE_HOME}/assets/tldr-book-fr.pdf" \
    "${SITE_HOME}/assets/tldr-book-hi.pdf" \
    "${SITE_HOME}/assets/tldr-book-id.pdf" \
    "${SITE_HOME}/assets/tldr-book-it.pdf" \
    "${SITE_HOME}/assets/tldr-book-ja.pdf" \
    "${SITE_HOME}/assets/tldr-book-ko.pdf" \
    "${SITE_HOME}/assets/tldr-book-lo.pdf" \
    "${SITE_HOME}/assets/tldr-book-ml.pdf" \
    "${SITE_HOME}/assets/tldr-book-ne.pdf" \
    "${SITE_HOME}/assets/tldr-book-nl.pdf" \
    "${SITE_HOME}/assets/tldr-book-no.pdf" \
    "${SITE_HOME}/assets/tldr-book-pl.pdf" \
    "${SITE_HOME}/assets/tldr-book-pt_BR.pdf" \
    "${SITE_HOME}/assets/tldr-book-pt_PT.pdf" \
    "${SITE_HOME}/assets/tldr-book-ro.pdf" \
    "${SITE_HOME}/assets/tldr-book-ru.pdf" \
    "${SITE_HOME}/assets/tldr-book-sh.pdf" \
    "${SITE_HOME}/assets/tldr-book-sr.pdf" \
    "${SITE_HOME}/assets/tldr-book-sv.pdf" \
    "${SITE_HOME}/assets/tldr-book-ta.pdf" \
    "${SITE_HOME}/assets/tldr-book-th.pdf" \
    "${SITE_HOME}/assets/tldr-book-tr.pdf" \
    "${SITE_HOME}/assets/tldr-book-uk.pdf" \
    "${SITE_HOME}/assets/tldr-book-uz.pdf" \
    > "${SITE_HOME}/assets/tldr.sha256sums"

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
