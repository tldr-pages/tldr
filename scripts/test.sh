#!/usr/bin/env bash
# SPDX-License-Identifier: MIT

# This script has some basic tests for pages and scripts. If the build is also a PR, additional
# checks are run through the check-pr script, and any message or error is sent
# to tldr-bot to be commented on the PR.
#
# NOTE: must be run from the repository root directory to correctly work!
# NOTE: `set -e` is applied conditionally only if needed.

# check if a command is available to run in the system
function exists {
  command -v "$1" >/dev/null 2>&1
}

# Wrapper around black as it outputs everything to stderr,
# but we want to only print if there are actual errors, and not
# the "All done!" success message.
function run_black {
  target_black_version=$(awk -F '==' '$1 == "black" { print $2 }' < requirements.txt)

  # skip the black check if the command is not available in the system.
  if [[ $CI != true ]] && ! exists black; then
    echo "Skipping black check, command not available."
    return 0
  fi

  if grep -qw black <<< "$(pip3 --disable-pip-version-check list)"; then
    for script in $1; do
      errs="$(black $script -q --check --required-version ${target_black_version} 2>&1 || true)"
      if [[ ${errs} == *"does not match the running version"* ]]; then
        echo -e "Skipping black check, required version not available, try running: pip3 install -r requirements.txt"
        return 0
      fi

      # We want to ignore the exit code from black on failure so that we can
      # do the conditional printing below
      if [[ ${errs} != "" ]]; then
        echo -e "${errs}" >&2
        return 1
      fi
    done
  fi
}

function run_flake8 {
  # skip flake8 check if the command is not available in the system.
  if [[ $CI != true ]] && ! exists flake8; then
    echo "Skipping flake8 check, command not available."
    return 0
  fi

  for script in $1; do
    flake8 $script
  done
}

function run_pytest {
  # skip pytest check if the command is not available in the system.
  if [[ $CI != true ]] && ! exists pytest; then
    echo "Skipping pytest check, command not available."
    return 0
  fi

  errs=$(pytest $1 2>&1 || true)
  if [[ ${errs} == *"failed"* ]]; then
    echo -e "${errs}" >&2
    return 1
  fi
}

function test_pages {
  for f in $1; do
    markdownlint $1
    if [[ $f != *pages/* ]]; then
      checks="TLDR104"
    fi
  
    if [[ -L $f ]]; then
        continue
    elif [[ $f == *ar* || $f == *bn* || $f == *fa* || $f == *hi* || $f == *ja* || $f == *ko* || $f == *lo* || $f == *ml* || $f == *ne* || $f == *ta* || $f == *th* || $f == *tr* ]]; then
        checks+=",TLDR003,TLDR004,TLDR015"
    elif [[ $f == *zh* || $f == *zh_TW* ]]; then
        checks+=",TLDR003,TLDR004,TLDR005,TLDR015"
    fi
    tldr-lint --ignore $checks "${f}"
  done
}

function test_python_scripts {
    run_black $1
    run_flake8 $1
    run_pytest $1
}

# Default test function, run by `npm test`
# Tests all pages and scripts in the repository
function run_all_tests_full_repo {
  test_pages "./pages" "./pages.*"
  test_python_scripts "scripts/*.py"
}
