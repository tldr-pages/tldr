#!/usr/bin/env bash
# SPDX-License-Identifier: MIT

# This script is executed by GitHub Actions for every successful push (on any branch, PR or not).
# It runs some basic tests on pages. If the build is also a PR, additional
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
  # skip black check if command is not available in the system.
  if [ "$CI" != "true" ] && ! exists black; then
    echo "Skipping black check, command not available."
    return 0
  fi

  # we want to ignore the exit code from black on failure, so that we can
  # do the conditional printing below
  errs=$(black scripts --check 2>&1 || true)
  if [[ ${errs} != "All done!"* ]]; then
     echo -e "${errs}" >&2
     return 1
  fi
}

function run_flake8 {
  # skip flake8 check if command is not available in the system.
  if [ "$CI" != "true" ] && ! exists flake8; then
    echo "Skipping flake8 check, command not available."
    return 0
  fi

  flake8 scripts
}

# Default test function, ran by `npm test`.
function run_tests {
  markdownlint pages*/**/*.md
  tldr-lint ./pages
  for f in ./pages.*; do
    tldr-lint --ignore "TLDR003,TLDR004,TLDR005,TLDR015,TLDR104" "${f}"
  done
  run_black
  run_flake8
}

# Special test function for GitHub Actions pull request builds.
# Runs run_tests collecting errors for tldr-bot.
function run_tests_pr {
  errs=$(run_tests 2>&1)

  if [ -n "$errs" ]; then
    echo -e "Test failed!\n$errs\n" >&2
    echo 'Sending errors to tldr-bot.' >&2
    echo -n "$errs" | python3 scripts/send-to-bot.py report-errors
    exit 1
  fi
}

# Additional checks for GitHub Actions pull request builds.
# Only taken as suggestions, does not make the build fail.
function run_checks_pr {
  msgs=$(bash scripts/check-pr.sh)

  if [ -n "$msgs" ]; then
    echo -e "\nCheck PR reported the following message(s):\n$msgs\n" >&2
    echo 'Sending check results to tldr-bot.' >&2
    echo -n "$msgs" | python3 scripts/send-to-bot.py report-check-results
  fi
}

###################################
# MAIN
###################################

if [ "$CI" = "true" ] && [ "$GITHUB_REPOSITORY" = "tldr-pages/tldr" ] && [ "$PULL_REQUEST_ID" != "" ]; then
  run_checks_pr
  run_tests_pr
else
  set -e
  run_tests
fi

echo 'Test ran successfully!'
