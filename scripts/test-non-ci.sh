#!/usr/bin/env bash
# SPDX-License-Identifier: MIT

# This script is the entrypoint for test.sh.
#
# NOTE: must be run from the repository root directory to correctly work!
# NOTE: `set -e` is applied conditionally only if needed.

source "$(dirname "${BASH_SOURCE[0]}")/test.sh"

# check if a command is available to run in the system
function exists {
  command -v "$1" >/dev/null 2>&1
}

function check_for_unstaged_changes {
  if [[ $(git ls-files --modified) != "" ]]; then
    echo 'There are unstaged changes! Stashing them...'
    git stash --keep-index --include-untracked
  fi
  return 0
}

function test_python_scripts {
    run_black $1
    run_flake8 $1
}

# Special test function for changes staged for a commit.
# Run by 'npm test' if $COMMIT is set to true.
function run_tests_commit {
  pages="$(git diff --cached --name-only | grep '^pages/' || true)"
  echo "testing pages"
  if [[ $pages != "" ]]; then
    test_pages "$pages"
  fi
  echo 'done pages'
  scripts="$(git diff --cached --name-only | awk '/^scripts/ && /.py$/')"
  if [[ $scripts != "" ]]; then
    test_python_scripts "$scripts"
  fi
}

###################################
# MAIN
###################################

set -e

stash_pop=1

if [[ $COMMIT == true ]]; then
  if [[ $(git diff --cached --name-only) != "" ]]; then
    check_for_unstaged_changes
    stash_pop=$?
    run_tests_commit
  else
    echo 'No files to test, add files to test them.'
    exit 0
  fi
else
  run_all_tests
fi

if [[ $stash_pop == 0 ]]; then
  git stash pop
fi

echo 'Test ran successfully!'
