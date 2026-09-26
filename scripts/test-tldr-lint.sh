#!/usr/bin/env bash
# SPDX-License-Identifier: MIT

# This helper script was split out of function run_tests in test.sh
# so that it can be parallelized

checks="TLDR104"
case $1 in
  *ar*|*bn*|*fa*|*hi*|*ja*|*ko*|*lo*|*ml*|*ne*|*ta*|*th*|*tr*)
    checks+=",TLDR003,TLDR004,TLDR015"
  ;;
  *zh*)
    checks+=",TLDR003,TLDR004,TLDR005,TLDR015"
  ;;
  *en*)
    # Don't ignore anything for the `pages.en` symlink.
    checks=""
    # "pages.en" -> "pages"
    set -- "pages"
  ;;
esac
exec npx tldr-lint --ignore "$checks" "$1"
