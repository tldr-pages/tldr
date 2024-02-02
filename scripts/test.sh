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

function check_for_unstaged_changes {
  if [[ $(git ls-files --modified) != "" ]]; then
    echo 'There are unstaged changes!'
    read -n1 -p '[a]dd, [d]iscard, [s]tash them or [q]uit? ' resp && echo ''
    case ${resp} in
      a)
        git add .
        ;;
      d)
        git restore .
        ;;
      s)
        git stash -k --include-untracked
        ;;
      q)
        exit 1
        ;;
      *)
        echo 'Unknown option! Quitting...'
        exit 1
        ;;
    esac
  fi
}

# Wrapper around black as it outputs everything to stderr,
# but we want to only print if there are actual errors, and not
# the "All done!" success message.
function run_black {
  target_black_version=$(awk -F '==' '$1 == "black" { print $2 }' < requirements.txt)

  if grep -qw black <<< "$(pip3 --disable-pip-version-check list)"; then
    errs=$(python3 -m black scripts -q --check --required-version ${target_black_version} 2>&1 || true)
  fi

  if [[ -z $errs ]]; then
    # skip the black check if the command is not available in the system.
    if ! exists black; then
      echo "Skipping black check, command not available."
      return 0
    fi
    for script in $1; do
      errs="$(black $script --check --required-version ${target_black_version} 2>&1 || true)"
      if [[ ${errs} == *"does not match the running version"* ]]; then
        echo -e "Skipping black check, required version not available, try running: pip3 install -r requirements.txt"
        return 0
      fi

      # We want to ignore the exit code from black on failure so that we can
      # do the conditional printing below
      if [[ ${errs} != "All done!"* ]]; then
        echo -e "${errs}" >&2
        return 1
      fi
    done
  fi
}

function run_flake8 {
  # skip flake8 check if the command is not available in the system.
  if ! exists flake8; then
    echo "Skipping flake8 check, command not available."
    return 0
  fi

  for script in $1; do
    flake8 $script
  done
}

function test_pages {
  for f in $1; do
    checks="TLDR003,TLDR004,TLDR015,TLDR104"
    if [[ -L $f ]]; then
        continue
    elif [[ $f == *zh* || $f == *zh_TW* ]]; then
        checks+=",TLDR005"
    fi
    tldr-lint --ignore $checks "${f}"
  done
}

function test_python_scripts {
    run_black $1
    run_flake8 $1
}

# Default test function, run by `npm test`.
function run_tests {
  find pages* -name '*.md' -exec markdownlint {} +
  tldr-lint ./pages
  test_pages "./pages.*"
  if [[ $CI != true ]]; then
    test_python_scripts "scripts/*.py"
  fi
}

# Special test function for changes staged for a commit.
# Run by 'npm test' if $COMMIT is set to true.
function run_tests_commit {
  pages="$(git diff --cached --name-only | grep '^pages/' || true)"
  if [[ $pages != "" ]]; then
    test_pages "$pages"
  fi
  scripts="$(git diff --cached --name-only | awk '/^scripts/ && /.py$/')"
  if [[ $scripts != "" ]]; then
    test_python_scripts "$scripts"
  fi
}

# Special test function for GitHub Actions pull request builds.
# Runs run_tests collecting errors for tldr-bot.
function run_tests_pr {
  errs=$(run_tests 2>&1)

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
else
  set -e
  if [[ $COMMIT == true ]]; then
    if [[ $(git diff --cached --name-only) != "" ]]; then
      check_for_unstaged_changes
      run_tests_commit
    else
      echo 'No files to test, add files to test them.'
      exit 0
    fi
  else
    run_tests
  fi
fi

echo 'Test ran successfully!'
