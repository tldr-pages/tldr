#!/usr/bin/env bash
# SPDX-License-Identifier: MIT

# This script is executed by GitHub Actions for every pull request opened.
# It currently accomplishes the following objectives:
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
  local page=$1 # page path in the format 'platform/pagename.md'
  local parts
  local other

  readarray -td'/' parts < <(echo -n "$page")

  local platform=${parts[0]}
  local file=${parts[1]}

  case "$platform" in
    common) # check if page already exists in other platforms
      for other in ${PLATFORMS/common/}; do
        if [[ -f "pages/$other/$file" ]]; then
          printf "\x2d $MSG_EXISTS" "$page" "$other"
        fi
      done
      ;;

    *) # check if page already exists under common
      if [[ -f "pages/common/$file" ]]; then
        printf "\x2d $MSG_EXISTS" "$page" 'common'
      fi
      ;;
  esac
}

# Look at git diff and check for copied/duplicated pages.
function check_diff {
  local git_diff
  local line
  local entry

  git_diff=$(git diff --name-status --find-copies-harder --diff-filter=AC origin/main -- pages*/)

  if [[ -n $git_diff ]]; then
    echo -e "Check PR: git diff:\n$git_diff" >&2
  else
    echo 'Check PR: git diff looks fine, no interesting changes detected.' >&2
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

        printf "\x2d $MSG_IS_COPY" "$file2" "$file1" "$percentage"
        ;;

      A) # file1 was newly added
        check_duplicates "$file1"
        ;;
    esac
  done <<< "$git_diff"
}

# Recursively check the pages/ folder for anomalies.
function check_structure {
  for platform in $PLATFORMS; do
    if [[ ! -d "pages/$platform" ]]; then
      printf "\x2d $MSG_NOT_DIR" "pages/$platform"
    else
      for page in "pages/$platform"/*; do
        if [[ ! -f $page ]]; then
          printf "\x2d $MSG_NOT_FILE" "$page"
        elif [[ ${page:(-3)} != ".md" ]]; then
          printf "\x2d $MSG_NOT_MD" "$page"
        fi
      done
    fi
  done
}

###################################
# MAIN
###################################

MSG_EXISTS='The page `%s` already exists under the `%s` platform.\n'
MSG_IS_COPY='The page `%s` seems to be a copy of `%s` (%d%% matching).\n'
MSG_NOT_DIR='The file `%s` does not look like a directory.\n'
MSG_NOT_FILE='The file `%s` does not look like a regular file.\n'
MSG_NOT_MD='The file `%s` does not have a `.md` extension.\n'

PLATFORMS=$(ls pages/)

if [[ $CI == true && $GITHUB_REPOSITORY == "tldr-pages/tldr" && $PULL_REQUEST_ID != "" ]]; then
  check_diff
  check_structure
else
  echo 'Not a pull request, refusing to run.' >&2
  exit 0
fi
