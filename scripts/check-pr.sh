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
#  4. Detect pages that do not exist as English pages yet.
#  5. Detect outdated pages. A page is marked as outdated when the number of 
#     commands differ from the number of commands in the English page or the
#     contents of the commands differ from the English page.
#  6. Detect other miscellaneous anomalies in the pages folder.
#
# Results are printed to stdout, logs and errors to stderr.
#
# NOTE: must be run from the repository root directory to correctly work!
# NOTE: no `set -e`, failure of this script should not invalidate the build.

# Check for duplicated pages.
function check_duplicates {
  local page=$1 # page path in the format 'pages<.language_code>/platform/pagename.md'
  local parts
  local other

  readarray -td'/' parts < <(echo -n "$page")

  local language_folder=${parts[0]}
  
  if [[ "$language_folder" != "pages" ]]; then # only check for duplicates in English
    return 1
  fi

  local platform=${parts[1]}
  local file=${parts[2]}

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

function check_missing_english_page() {
  local page=$1
  local english_page="pages/${page#pages*\/}"

  if [[ "$page" = "$english_page" ]]; then
    return 1
  fi
  
  if [[ ! -f "$english_page" ]]; then
    printf "\x2d $MSG_NOT_EXISTS" "$page" "$english_page"
  fi
}

function count_commands() {
  local file="$1"
  local regex="$2"

  grep -c "$regex" "$file"
}

function strip_commands() {
  local file="$1"
  local regex="$2"

  local stripped_commands=()

  mapfile -t stripped_commands < <(
    grep "$regex" "$file" | 
    sed 's/{{[^}]*}}/{{}}/g' | 
    sed 's/<[^>]*>//g' | 
    sed 's/([^)]*)//g' | 
    sed 's/"[^"]*"/""/g' | 
    sed "s/'[^']*'//g" | 
    sed 's/`//g'
  )

  printf "%s\n" "${stripped_commands[*]}"
}

function check_outdated_page() {
  local page=$1
  local english_page="pages/${page#pages*\/}"
  local command_regex='^`[^`]\+`$'

  if [[ "$page" = "$english_page" ]] || [[ ! -f "$english_page" ]]; then
    return 1
  fi

  local english_commands
  english_commands=$(count_commands "$english_page" "$command_regex")
  local commands
  commands=$(count_commands "$page" "$command_regex")

  local english_commands_as_string
  english_commands_as_string=$(strip_commands "$english_page" "$command_regex")
  local commands_as_string
  commands_as_string=$(strip_commands "$page" "$command_regex")
  
  if [[ "$english_commands" != "$commands" ]]; then
    printf "\x2d $MSG_OUTDATED" "$page" "based on number of commands"
  elif [[ "$english_commands_as_string" != "$commands_as_string" ]]; then
    printf "\x2d $MSG_OUTDATED" "$page" "based on the command contents itself"
  fi
}

# Look at git diff and check for copied/duplicated pages.
function check_diff {
  local git_diff
  local line
  local entry

  git_diff=$(git diff --name-status --find-copies-harder --diff-filter=ACM origin/main -- pages*/)

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

      A|M) # file1 was newly added or modified
        check_duplicates "$file1"
        check_missing_english_page "$file1"
        check_outdated_page "$file1"
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
MSG_NOT_EXISTS='The page `%s` does not exists as English page `%s` yet.\n'
MSG_OUTDATED='The page `%s` is outdated, %s.\n'
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
