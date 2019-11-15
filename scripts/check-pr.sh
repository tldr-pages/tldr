#!/usr/bin/env bash

# This script is executed by Travis CI for every pull request opened.
# It currently accomplishes the following objectives (for English pages only):
#
#  1. Detect pages that were just copied (i.e. cp pages/{common,linux}/7z.md).
#  2. Detect pages that were added in a platform specific directory although
#     they already exist under 'common'.
#  3. Detect pages that were added in the 'common' platform although they
#     already exist under a platform specific directory.
#  4. Detect other miscellaneous anomalies in the pages folder.
#
# Results are printed to stdout, logs and errors to stderr.
#
# NOTE: must be run from the repository root directory to correctly work!
# NOTE: no `set -e`, failure of this script should not invalidate the build.

# Check for duplicated pages.
function check_duplicates {
  local msg='The page `%s` already exists under the `%s` platform.\n'
  local page=$1 # page path in the format 'platform/pagename.md'
  local parts
  local other

  readarray -td'/' parts < <(echo -n "$page")

  local platform=${parts[0]}
  local file=${parts[1]}

  case "$platform" in
    common) # check if page already exists in other platforms
      for other in `ls pages/`; do
        if [ "$other" != 'common' ]; then
          if [ -f "pages/$other/$file" ]; then
            printf "\x2d $msg" "$page" "$other"
          fi
        fi
      done
      ;;

    *) # check if page already exists under common
      if [ -f "pages/common/$file" ]; then
        printf "\x2d $msg" "$page" 'common'
      fi
      ;;
  esac
}

# Look at git diff and check for copied/duplicated pages.
function check_diff {
  local msg='The page `%s` seems to be a copy of `%s` (%d%% matching).\n'
  local git_diff
  local line
  local entry

  git_diff=`git diff --name-status --find-copies-harder --diff-filter=AC --relative=pages/ master`

  if [ -n "$git_diff" ]; then
    echo -e "Check PR: git diff:\n$git_diff" >&2
  else
    echo 'Check PR: looks fine, no interesting changes detected.' >&2
    return 0
  fi

  while read line; do
    readarray -td$'\t' entry < <(echo -n "$line")

    local change="${entry[0]}"
    local file1="${entry[1]}"
    local file2="${entry[2]}"

    case "$change" in
      C*) # file2 is a copy of file1
        local percentage=${change#C}
        percentage=${percentage#0}
        percentage=${percentage#0}

        printf "\x2d $msg" "$file2" "$file1" "$percentage"
        ;;

      A) # file1 was newly added
        check_duplicates "$file1"
        ;;
    esac
  done <<< "$git_diff"
}

# Recursively check the pages/ folder for anomalies.
function check_structure {
  local msg_not_dir='The file `%s` does not look like a directory.\n'
  local msg_not_file='The file `%s` does not look like a regular file.\n'
  local msg_not_md='The file `%s` does not have a `.md` extension.\n'

  for platform in pages/*; do
    if [ ! -d "$platform" ]; then
      printf "\x2d $msg_not_dir" "$platform"
    else
      for page in "$platform"/*; do
        if [ ! -f "$page" ]; then
          printf "\x2d $msg_not_file" "$page"
        elif [ "${page:(-3)}" != ".md" ]; then
          printf "\x2d $msg_not_md" "$page"
        fi
      done
    fi
  done
}

###################################
# MAIN
###################################

if [ "$TRAVIS" = "true" ] && [ "$TRAVIS_REPO_SLUG" = "tldr-pages/tldr" ] && [ "$TRAVIS_PULL_REQUEST" != "false" ]; then
  check_diff
  check_structure
else
  echo 'Not a pull request, refusing to run.' >&2
  exit 0
fi
