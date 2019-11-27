#!/usr/bin/env bash

# This script is executed by Travis CI for every successful push (on any branch, PR or not).
# It runs some basic tests on pages. If the build is also a PR, additional
# checks are run through the check-pr script, and any message or error is sent
# to tldr-bot to be commented on the PR.
#
# NOTE: must be run from the repository root directory to correctly work!
# NOTE: `set -e` is applied conditionally only if needed.

# Default test function, ran by `npm test`.
function run_tests {
  markdownlint pages*/**/*.md
  tldr-lint ./pages
}

# Special test function for Travis CI pull request builds.
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

# Additional checks for Travis CI pull request builds.
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

if [ "$TRAVIS" = "true" ] && [ "$TRAVIS_REPO_SLUG" = "tldr-pages/tldr" ] && [ "$TRAVIS_PULL_REQUEST" != "false" ]; then
  run_checks_pr
  run_tests_pr
else
  set -e
  run_tests
fi

echo 'Test ran succesfully!'
