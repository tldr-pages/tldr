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

function run_all_tests_pr {
  local git_diff
  local line
  local entry

  git_diff=$(git diff --name-status --find-copies-harder --diff-filter=ACM origin/main -- pages/ pages*/ scripts/)
  if [[ -n $git_diff ]]; then
    echo 'No changes were made.' >&2
    return 0
  else
    echo 'Changes were made'
    return 0
  fi
  
  while read line; do
    readarray -td$'\t' entry < <(echo -n "$line")

    local file1="${entry[1]}"
    local file2="${entry[2]}"

    echo "Testing $file1 and $file2"
    if [ $file1 == *.md* ]; then
      test_pages "$file1 $file2"
    fi
    if [ $file1 == *.py* ]; then
      echo 'Found a script'
      test_python_scripts "$file1 $file2"
    fi
  done <<< "$git_diff"  
}

# Special test function for GitHub Actions pull request builds.
# Runs run_all_tests_pr collecting errors for tldr-bot.
function run_tldr_bot_tests {
  errs=$(run_all_tests_pr 2>&1)

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
  run_tldr_bot_tests
fi

echo 'Test ran successfully!'
