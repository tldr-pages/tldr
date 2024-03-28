#!/usr/bin/env bash
# SPDX-License-Identifier: MIT

# This script is executed by GitHub Actions for every successful push (on any branch, PR or not).
# It is the CI entrypoint for test.sh.
#
# NOTE: must be run from the repository root directory to correctly work!
# NOTE: `set -e` is applied conditionally only if needed.

source "$(dirname "${BASH_SOURCE[0]}")/test.sh"

# check if a command is available to run in the system
function exists {
  command -v "$1" >/dev/null 2>&1
}

# Special test function for GitHub Actions pull request builds.
# Runs run_tests collecting errors for tldr-bot.
function run_tests_pr {
  errs=$(run_all_tests 2>&1)

  if [[ -n $errs ]]; then
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

  if [[ -n $msgs ]]; then
    echo -e "\nCheck PR reported the following message(s):\n$msgs\n" >&2
    echo 'Sending check results to tldr-bot.' >&2
    echo -n "$msgs" | python3 scripts/send-to-bot.py report-check-results
  fi
}

###################################
# MAIN
###################################

if [[ $CI == true && $GITHUB_REPOSITORY == "tldr-pages/tldr" && $PULL_REQUEST_ID != "" ]]; then
  run_checks_pr
  run_tests_pr
fi

echo 'Test ran successfully!'
