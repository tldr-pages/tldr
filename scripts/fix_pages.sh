#!/usr/bin/env bash

declare RESET_COLOR='\e[0m'
declare RED_COLOR='\e[31m'
declare GREEN_COLOR='\e[32m'
declare YELLOW_COLOR='\e[33m'
declare BLUE_COLOR='\e[34m'
declare MAGENTA_COLOR='\e[35m'
declare CYAN_COLOR='\e[36m'

declare BACKGROUND_RED_COLOR='\e[41m'
declare BACKGROUND_GREEN_COLOR='\e[42m'
declare BACKGROUND_YELLOW_COLOR='\e[43m'
declare BACKGROUND_BLUE_COLOR='\e[44m'
declare BACKGROUND_MAGENTA_COLOR='\e[45m'
declare BACKGROUND_CYAN_COLOR='\e[46m'

declare -A FUNCTION_ASSOCIATIONS=(
  [descriptions:stream]=fix_io_stream_names_action
  [descriptions:see-also]=fix_see_also_links_action
  [generic-placeholder-naming:file]=fix_generic_file_placeholders_action
  [generic-placeholder-naming:directory]=fix_generic_directory_placeholders_action
  [placeholder-naming:file]=fix_file_placeholders_action
  [generic-placeholder-quoting:file]=fix_generic_file_placeholder_quoting_action
  [generic-placeholder-quoting:directory]=fix_generic_directory_placeholder_quoting_action
  [any-placeholder-grouping:any]=fix_placeholder_ellipsis_action
)

help() {
  echo -e "${BLUE_COLOR}TlDr page fixer.$RESET_COLOR

${MAGENTA_COLOR}Usage:$RESET_COLOR
  $CYAN_COLOR$0$RESET_COLOR ${YELLOW_COLOR}[(-nd|--no-description)] [(-np|--no-placeholder)] [(-nq|--no-quiet)] [(-nnq|--non-noquiet)] [(-ncf|--no-confirmation-for) <value>]
  $CYAN_COLOR$0$RESET_COLOR ${YELLOW_COLOR}(-h|--help)
  $CYAN_COLOR$0$RESET_COLOR ${YELLOW_COLOR}(-v|--version)

${MAGENTA_COLOR}Options:$RESET_COLOR
  $CYAN_COLOR-h --help                  ${BLUE_COLOR}Display this help.
  $CYAN_COLOR-v --version               ${BLUE_COLOR}Display the version.
  $CYAN_COLOR-nd --no-description       ${BLUE_COLOR}Don't fix command and example descriptions.
  $CYAN_COLOR-np --no-placeholder       ${BLUE_COLOR}Don't fix code placeholders.
  $CYAN_COLOR-nq --no-quiet             ${BLUE_COLOR}Don't apply fixes without confirmation.
  $CYAN_COLOR-nnq --no-non-quiet        ${BLUE_COLOR}Don't apply fixes with confirmation.
  $CYAN_COLOR-ncf --no-confirmation-for ${BLUE_COLOR}Apply specific fixes without confirmation.
                               ${RED_COLOR}Valid values: ${GREEN_COLOR}descriptions:${YELLOW_COLOR}stream ${GREEN_COLOR}descriptions:${YELLOW_COLOR}see-also
                                             ${GREEN_COLOR}generic-placeholder-naming:${YELLOW_COLOR}file ${GREEN_COLOR}generic-placeholder-naming:${YELLOW_COLOR}directory ${GREEN_COLOR}placeholder-naming:${YELLOW_COLOR}file
                                             ${GREEN_COLOR}generic-placeholder-quoting:${YELLOW_COLOR}file ${GREEN_COLOR}generic-placeholder-quoting:${YELLOW_COLOR}directory
                                             ${GREEN_COLOR}any-placeholder-grouping:${YELLOW_COLOR}any$RESET_COLOR"
}

version() {
  echo "version: 1.0.0, author: Emily Grace Seville (EmilySeville7cfg@gmail.com)"
}

try_confirm() {
  declare message="$1"
  declare answer
  read -r -n 1 -p "$message [y/n]: " answer
  echo

  if [[ ! $answer =~ [yn] ]]; then
    answer=n
  fi

  if [[ $answer == n ]]; then
    return 1
  fi

  return 0
}

show_page_error() {
  declare page="$1"
  declare source="$2"
  declare fix="$3"

  if [[ $source != @(description|placeholder|quoting) ]]; then
    source="<unknown source>"
  fi

  if [[ -z $fix ]]; then
    fix="not available"
  fi

  echo -e "${BACKGROUND_RED_COLOR}error$RESET_COLOR in $CYAN_COLOR'${BLUE_COLOR}$page$CYAN_COLOR'$RESET_COLOR: ${YELLOW_COLOR}incorrect $source$RESET_COLOR, ${BACKGROUND_GREEN_COLOR}fix$RESET_COLOR: ${YELLOW_COLOR}$fix$RESET_COLOR "
}

show_page_warning() {
  declare page="$1"
  declare source="$2"
  declare fix="$3"

  if [[ $source != @(description|placeholder|quoting) ]]; then
    source="<unknown source>"
  fi

  if [[ -z $fix ]]; then
    fix="not available"
  fi

  echo -e "${BACKGROUND_MAGENTA_COLOR}warning$RESET_COLOR in $CYAN_COLOR'${BLUE_COLOR}$page$CYAN_COLOR'$RESET_COLOR: ${YELLOW_COLOR}possibly incorrect $source$RESET_COLOR, ${BACKGROUND_GREEN_COLOR}fix$RESET_COLOR: ${YELLOW_COLOR}$fix$RESET_COLOR "
}

show_page_info() {
  declare page="$1"
  declare source="$2"
  declare fix="$3"

  if [[ $source != @(ignored) ]]; then
    source="<unknown source>"
  fi

  if [[ -z $fix ]]; then
    fix="not available"
  fi

  echo -e "${BACKGROUND_CYAN_COLOR}info$RESET_COLOR about $CYAN_COLOR'${BLUE_COLOR}$page$CYAN_COLOR'$RESET_COLOR: ${YELLOW_COLOR}maybe should not be $source$RESET_COLOR, ${BACKGROUND_GREEN_COLOR}fix$RESET_COLOR: ${YELLOW_COLOR}$fix$RESET_COLOR "
}

show_argument_error() {
  declare argument="$1"
  declare source="$2"
  declare fix="$3"

  if [[ $source != @(option|value) ]]; then
    source="<unknown source>"
  fi

  if [[ -z $fix ]]; then
    fix="not available"
  fi

  echo -e "${BACKGROUND_RED_COLOR}argument error$RESET_COLOR in $CYAN_COLOR'${BLUE_COLOR}$argument$CYAN_COLOR'$RESET_COLOR: ${YELLOW_COLOR}incorrect $source$RESET_COLOR, ${BACKGROUND_GREEN_COLOR}fix$RESET_COLOR: ${YELLOW_COLOR}$fix$RESET_COLOR "
}

show_action_info() {
  declare action="$1"
  declare source="$2"
  declare fix="$3"

  if [[ $source != @(ignored) ]]; then
    source="<unknown source>"
  fi

  if [[ -z $fix ]]; then
    fix="not available"
  fi

  echo -e "${BACKGROUND_CYAN_COLOR}action info$RESET_COLOR about $CYAN_COLOR'${BLUE_COLOR}$action$CYAN_COLOR'$RESET_COLOR: ${YELLOW_COLOR}maybe should not be $source$RESET_COLOR, ${BACKGROUND_GREEN_COLOR}fix$RESET_COLOR: ${YELLOW_COLOR}$fix$RESET_COLOR "
}

declare IGNORE_FILE="$HOME/.config/fix_pages/ignore"

try_create_ignore_file() {
  declare directory="$(dirname "$IGNORE_FILE")"
  if [[ ! -d $directory ]]; then
    mkdir --parents "$directory" || {
      echo "Failed: to create ignore file." >&2
      exit 1
    }
    touch "$IGNORE_FILE"
  fi
}

clear_ignore_file() {
  echo > "$IGNORE_FILE" || echo "Failed: to clear ignore file." >&2
}

is_ignored() {
  declare page="$1"
  if grep -- "$page" "$IGNORE_FILE" > /dev/null; then
    return 0;
  fi
  return 1
}

ignore() {
  declare page="$1"
  echo "$page" >> "$IGNORE_FILE"
}


parse_see_also_links() {
  declare line="$1"
  echo "$line" |\
    sed --regexp-extended "s/ *\.\$//; s/^> See also: *(.+)/\1/; s/ +/ /g; s/[\`\"']//g; s/ +(or|and) +//g; s/,/\n/g" |\
    sed --regexp-extended --quiet "s/^ +//; s/ +$//; /^\s+$/!p;" |\
    sed --regexp-extended "/^[[:space:]]*$/d"
}

create_see_also_links() {
  if (( $# == 0 )); then
    return
  fi
  if (( $# == 1 )); then
    echo "> See also: \`$1\`."
    return
  fi
  if (( $# == 2 )); then
    echo "> See also: \`$1\` or \`$2\`."
    return
  fi

  declare see_also_line="> See also: \`$1\`"
  declare -i i=1
  shift
  for command in "$@"; do
    if (( i < $# )); then
      see_also_line+=", \`$command\`"
    else
      see_also_line+=", or \`$command\`."
    fi
    ((i++))
  done

  echo "$see_also_line"
}


# Use `stdin`, `stdout`, `stderr` keywords.
fix_io_stream_names_action() {
  for directory in *; do
    for page in "$directory"/*.md; do
      declare stream="^- (.*[^\`])([\"']?)std(in|out|err)\2"
      if grep --ignore-case --extended-regexp -- "$stream" "$page" > /dev/null; then
        show_page_error "$page" description "add backticks for stream name"
        if sed --in-place --regexp-extended "s/$stream/- \1\`std\L\3\E\`/gi" "$page"; then
          echo "Done."
        else
          echo "Failed: check whether file can be overridden."
        fi
      fi
    done
  done
}

# Use correct `See also` format.
fix_see_also_links_action() {
  for directory in *; do
    for page in "$directory"/*.md; do
      if is_ignored "$page"; then
        show_page_info "$page" ignored "remove it from '$IGNORE_FILE'."
        continue
      fi

      declare see_also="^> See also:"
      if grep --ignore-case --extended-regexp -- "$see_also" "$page" > /dev/null; then
        declare correct_format="^> See also: \`[^\`,]+\`( or \`[^\`,]+\`|(, \`[^\`,]+\`)+(, or \`[^\`,]+\`))?\.\$"
        
        if ! grep --ignore-case --extended-regexp -- "$correct_format" "$page" > /dev/null; then
          show_page_error "$page" description "add backticks for command names, remove extra spaces, use \`or\` before the last command"

          declare see_also_line="$(grep --ignore-case --extended-regexp -- "$see_also" "$page")"
          readarray -t links < <(parse_see_also_links "$see_also_line")

          if sed --in-place --regexp-extended "s/$see_also.*/$(create_see_also_links "${links[@]}")/g" "$page"; then
            echo "Done."
          else
            echo "Failed: check whether file can be overridden."
          fi
        fi
      fi
    done
  done
}

# Use `{{path/to/file}}` generic placeholders.
fix_generic_file_placeholders_action() {
  for directory in *; do
    for page in "$directory"/*.md; do
      if is_ignored "$page"; then
        show_page_info "$page" ignored "remove it from '$IGNORE_FILE'."
        continue
      fi

      declare with_extension='\{\{[^/ {]*file[^/ {]*([[:digit:]]*)\.([^ ]+)\}\}'
      if grep --extended-regexp "$with_extension" "$page" > /dev/null; then
        show_page_error "$page" placeholder "use \`{{path/to/file}}\` syntax with an optional trailing number before an extension"
        if sed --in-place --regexp-extended "s/$with_extension/{{path\/to\/file\1.\2}}/g" "$page"; then
          echo "Done."
        else
          echo "Failed: check whether file can be overridden."
        fi
      fi

      declare without_extension='\{\{[^/ {]*file[^/ {]*([[:digit:]]*)\}\}'
      if grep --extended-regexp "$without_extension" "$page" > /dev/null; then
        show_page_error "$page" placeholder "use \`{{path/to/file}}\` syntax with an optional trailing number"
        if sed --in-place --regexp-extended "s/$without_extension/{{path\/to\/file\1}}/g" "$page"; then
          echo "Done."
        else
          echo "Failed: check whether file can be overridden."
        fi
      fi
    done
  done
}

# Use `{{path/to/directory}}` generic placeholders.
fix_generic_directory_placeholders_action() {
  for directory in *; do
    for page in "$directory"/*.md; do
      if is_ignored "$page"; then
        show_page_info "$page" ignored "remove it from '$IGNORE_FILE'."
        continue
      fi

      declare without_extension='\{\{[^/ {]*dir(ectory)?[^/ {]*([[:digit:]]*)\}\}'
      if grep --extended-regexp "$without_extension" "$page" > /dev/null; then
        show_page_error "$page" placeholder "use \`{{path/to/directory}}\` syntax with an optional trailing number"
        if sed --in-place --regexp-extended "s/$without_extension/{{path\/to\/directory\2}}/g" "$page"; then
          echo "Done."
        else
          echo "Failed: check whether file can be overridden."
        fi
      fi
    done
  done
}

# Use `{{path/to/source}}`, `{{path/to/executable}}` placeholders.
fix_file_placeholders_action() {
  for directory in *; do
    for page in "$directory"/*.md; do
      if is_ignored "$page"; then
        show_page_info "$page" ignored "remove it from '$IGNORE_FILE'."
        continue
      fi
      
      declare with_extension='\{\{[^/ {]*(source|executable)[^/ {]*([[:digit:]]*)\.([^ ]+)\}\}'
      if grep --extended-regexp "$with_extension" "$page" > /dev/null; then
        show_page_error "$page" placeholder "use \`{{path/to/source}}\` or \`{{path/to/executable}}\` syntax with an optional trailing number before an extension"
        code "$page"

        if [[ ! " $* " =~ " ${FUNCNAME[0]} " ]]; then
          if ! try_confirm "Do you want to fix '$page'?"; then
            ignore "$page"
            continue
          fi
        fi

        if sed --in-place --regexp-extended "s/$with_extension/{{path\/to\/\1\2.\3}}/g" "$page"; then
          echo "Done."
        else
          echo "Failed: check whether file can be overridden."
        fi
      fi

      declare without_extension='\{\{[^/ {]*(source|executable)[^/ {]*([[:digit:]]*)\}\}'
      if grep --extended-regexp "$without_extension" "$page" > /dev/null; then
        show_page_error "$page" placeholder "use \`{{path/to/source}}\` or \`{{path/to/executable}}\` syntax with an optional trailing number"
        code "$page"

        if [[ ! " $* " =~ " ${FUNCNAME[0]} " ]]; then
          if ! try_confirm "Do you want to fix '$page'?"; then
            ignore "$page"
            continue
          fi
        fi

        if sed --in-place --regexp-extended "s/$without_extension/{{path\/to\/\1\2}}/g" "$page"; then
          echo "Done."
        else
          echo "Failed: check whether file can be overridden."
        fi
      fi
    done
  done
}

# Remove quotes for generic file placeholders.
# Assumption: placeholder contents are already fixed.
fix_generic_file_placeholder_quoting_action() {
  for directory in *; do
    for page in "$directory"/*.md; do
      if is_ignored "$page"; then
        show_page_info "$page" ignored "remove it from '$IGNORE_FILE'."
        continue
      fi

      declare with_extension="([\"'])(\{\{path\/to\/file[[:digit:]]*\.[^ ]+\}\})\1"
      if grep --extended-regexp "$with_extension" "$page" > /dev/null; then
        show_page_error "$page" quoting "remove quotes around path with an optional trailing number with an extension"
        if sed --in-place --regexp-extended "s/$with_extension/\2/g" "$page"; then
          echo "Done."
        else
          echo "Failed: check whether file can be overridden."
        fi
      fi

      declare without_extension="([\"'])(\{\{path\/to\/file[[:digit:]]*\}\})\1"
      if grep --extended-regexp "$without_extension" "$page" > /dev/null; then
        show_page_error "$page" quoting "remove quotes around path with an optional trailing number"
        if sed --in-place --regexp-extended "s/$without_extension/\2/g" "$page"; then
          echo "Done."
        else
          echo "Failed: check whether file can be overridden."
        fi
      fi
    done
  done
}

# Remove quotes for generic directory placeholders.
# Assumption: placeholder contents are already fixed.
fix_generic_directory_placeholder_quoting_action() {
  for directory in *; do
    for page in "$directory"/*.md; do
      if is_ignored "$page"; then
        show_page_info "$page" ignored "remove it from '$IGNORE_FILE'."
        continue
      fi

      declare without_extension="([\"'])(\{\{path\/to\/directory[[:digit:]]*\}\})\1"
      if grep --extended-regexp "$without_extension" "$page" > /dev/null; then
        show_page_error "$page" quoting "remove quotes around path with an optional trailing number"
        if sed --in-place --regexp-extended "s/$without_extension/\2/g" "$page"; then
          echo "Done."
        else
          echo "Failed: check whether file can be overridden."
        fi
      fi
    done
  done
}

# Remove quotes for number placeholders.
fix_number_placeholder_quoting_action() {
  for directory in *; do
    for page in "$directory"/*.md; do
      if is_ignored "$page"; then
        show_page_info "$page" ignored "remove it from '$IGNORE_FILE'."
        continue
      fi

      declare number="([\"'])\{\{([[:digit:]]+\.[[:digit:]]*|\.[[:digit:]]+)\}\}\1"
      if grep --extended-regexp "$number" "$page" > /dev/null; then
        show_page_error "$page" quoting "remove quotes around number"
        if sed --in-place --regexp-extended "s/$number/{{\2}}/g" "$page"; then
          echo "Done."
        else
          echo "Failed: check whether file can be overridden."
        fi
      fi
    done
  done
}

# Use `{{placeholder1 placeholder2 ...}}` syntax.
# Asks confirmation as some commands don't require such change: it may break there syntax.
# Warning: placeholder must not contain spaces to be recignized valid for substitution.
fix_placeholder_ellipsis_action() {
  for directory in *; do
    for page in "$directory"/*.md; do
      if is_ignored "$page"; then
        show_page_info "$page" ignored "remove it from '$IGNORE_FILE'."
        continue
      fi

      declare placeholder_with_plural_word_and_extension="\{\{(.+)\(s\)\.([^ ]+)\}\}"
      if grep --extended-regexp -- "$placeholder_with_plural_word_and_extension" "$page" > /dev/null; then
        show_page_warning "$page" placeholder "replace plural term in a placeholder with an extension with ellipsis"
        code "$page"

        if [[ ! " $* " =~ " ${FUNCNAME[0]} " ]]; then
          if ! try_confirm "Do you want to fix '$page'?"; then
            ignore "$page"
            continue
          fi
        fi
        
        if sed --in-place --regexp-extended "s/$placeholder_with_plural_word_and_extension/\{\{\11.\2 \12.\2 ...\}\}/g" "$page"; then
          echo "Done."
        else
          echo "Failed: check whether file can be overridden."
        fi
      fi

      declare placeholder_with_plural_word_and_without_extension="\{\{(.+)\(s\)\}\}"
      if grep --extended-regexp -- "$placeholder_with_plural_word_and_without_extension" "$page" > /dev/null; then
        show_page_warning "$page" placeholder "replace plural term in a placeholder with ellipsis"
        code "$page"

        if [[ ! " $* " =~ " ${FUNCNAME[0]} " ]]; then
          if ! try_confirm "Do you want to fix '$page'?"; then
            ignore "$page"
            continue
          fi
        fi
        
        if sed --in-place --regexp-extended "s/$placeholder_with_plural_word_and_without_extension/\{\{\11 \12 ...\}\}/g" "$page"; then
          echo "Done."
        else
          echo "Failed: check whether file can be overridden."
        fi
      fi

      declare placeholder_with_brace_expansion_and_extension="\{\{([^ {}]+)\{[[:digit:]]+(,[[:digit:]]+)*\}\.([^ ]+)\}\}"
      if grep --extended-regexp -- "$placeholder_with_brace_expansion_and_extension" "$page" > /dev/null; then
        show_page_warning "$page" placeholder "replace brace expansion in a placeholder with an extension with ellipsis"
        code "$page"

        if [[ ! " $* " =~ " ${FUNCNAME[0]} " ]]; then
          if ! try_confirm "Do you want to fix '$page'?"; then
            ignore "$page"
            continue
          fi
        fi
        
        if sed --in-place --regexp-extended "s/$placeholder_with_brace_expansion_and_extension/\{\{\11.\3 \12.\3 ...\}\}/g" "$page"; then
          echo "Done."
        else
          echo "Failed: check whether file can be overridden."
        fi
      fi

      declare placeholder_with_brace_expansion_and_without_extension="\{\{([^ {}]+)\{[[:digit:]]+(,[[:digit:]]+)*\}\}\}"
      if grep --extended-regexp -- "$placeholder_with_brace_expansion_and_without_extension" "$page" > /dev/null; then
        show_page_warning "$page" placeholder "replace brace expansion in a placeholder with ellipsis"
        code "$page"

        if [[ ! " $* " =~ " ${FUNCNAME[0]} " ]]; then
          if ! try_confirm "Do you want to fix '$page'?"; then
            ignore "$page"
            continue
          fi
        fi
        
        if sed --in-place --regexp-extended "s/$placeholder_with_brace_expansion_and_without_extension/\{\{\11 \12 ...\}\}/g" "$page"; then
          echo "Done."
        else
          echo "Failed: check whether file can be overridden."
        fi
      fi

      declare consecutive_placeholder_pair_with_numbering_with_extension="\{\{(.+)1\.([^ ]+)\}\} +\{\{\12\.\2\}\}( +\{\{\1[[:digit:]]+\.\2\}\})*"
      if grep --extended-regexp -- "$consecutive_placeholder_pair_with_numbering_with_extension" "$page" > /dev/null; then
        show_page_warning "$page" placeholder "replace two consequtive placeholders with extensions with ellipsis"
        code "$page"

        if [[ ! " $* " =~ " ${FUNCNAME[0]} " ]]; then
          if ! try_confirm "Do you want to fix '$page'?"; then
            ignore "$page"
            continue
          fi
        fi
        
        if sed --in-place --regexp-extended "s/$consecutive_placeholder_pair_with_numbering_with_extension/\{\{\11.\2 \12.\2 ...\}\}/g" "$page"; then
          echo "Done."
        else
          echo "Failed: check whether file can be overridden."
        fi
      fi

      declare consecutive_placeholder_pair_with_numbering_without_extension="\{\{(.+)1\}\} +\{\{\12\}\}( +\{\{\1[[:digit:]]+\}\})*"
      if grep --extended-regexp -- "$consecutive_placeholder_pair_with_numbering_without_extension" "$page" > /dev/null; then
        show_page_warning "$page" placeholder "replace two consequtive placeholders with ellipsis"
        code "$page"

        if [[ ! " $* " =~ " ${FUNCNAME[0]} " ]]; then
          if ! try_confirm "Do you want to fix '$page'?"; then
            ignore "$page"
            continue
          fi
        fi
        
        if sed --in-place --regexp-extended "s/$consecutive_placeholder_pair_with_numbering_without_extension/\{\{\11 \12 ...\}\}/g" "$page"; then
          echo "Done."
        else
          echo "Failed: check whether file can be overridden."
        fi
      fi

      declare consecutive_placeholder_pair_with_broken_numbering_with_extension="\{\{(.+)\.([^ ]+)\}\} +\{\{\12\.\2\}\}( +\{\{\1[[:digit:]]+\.\2\}\})*"
      if grep --extended-regexp -- "$consecutive_placeholder_pair_with_broken_numbering_with_extension" "$page" > /dev/null; then
        show_page_warning "$page" placeholder "replace two consequtive placeholders with extensions with ellipsis"
        code "$page"

        if [[ ! " $* " =~ " ${FUNCNAME[0]} " ]]; then
          if ! try_confirm "Do you want to fix '$page'?"; then
            ignore "$page"
            continue
          fi
        fi
        
        if sed --in-place --regexp-extended "s/$consecutive_placeholder_pair_with_broken_numbering_with_extension/\{\{\11.\2 \12.\2 ...\}\}/g" "$page"; then
          echo "Done."
        else
          echo "Failed: check whether file can be overridden."
        fi
      fi

      consecutive_placeholder_pair_with_broken_numbering_with_extension="\{\{(.+)\.([^ ]+)\}\} +\{\{\11\.\2\}\}( +\{\{\1[[:digit:]]+\.\2\}\})*"
      if grep --extended-regexp -- "$consecutive_placeholder_pair_with_broken_numbering_with_extension" "$page" > /dev/null; then
        show_page_warning "$page" placeholder "replace two consequtive placeholders with extensions with ellipsis"
        code "$page"

        if [[ ! " $* " =~ " ${FUNCNAME[0]} " ]]; then
          if ! try_confirm "Do you want to fix '$page'?"; then
            ignore "$page"
            continue
          fi
        fi
        
        if sed --in-place --regexp-extended "s/$consecutive_placeholder_pair_with_broken_numbering_with_extension/\{\{\11.\2 \12.\2 ...\}\}/g" "$page"; then
          echo "Done."
        else
          echo "Failed: check whether file can be overridden."
        fi
      fi

      declare consecutive_placeholder_pair_with_broken_numbering_without_extension="\{\{(.+)\}\} +\{\{\12\}\}( +\{\{\1[[:digit:]]+\}\})*"
      if grep --extended-regexp -- "$consecutive_placeholder_pair_with_broken_numbering_without_extension" "$page" > /dev/null; then
        show_page_warning "$page" placeholder "replace two consequtive placeholders with ellipsis"
        code "$page"

        if [[ ! " $* " =~ " ${FUNCNAME[0]} " ]]; then
          if ! try_confirm "Do you want to fix '$page'?"; then
            ignore "$page"
            continue
          fi
        fi
        
        if sed --in-place --regexp-extended "s/$consecutive_placeholder_pair_with_broken_numbering_without_extension/\{\{\11 \12 ...\}\}/g" "$page"; then
          echo "Done."
        else
          echo "Failed: check whether file can be overridden."
        fi
      fi

      consecutive_placeholder_pair_with_broken_numbering_without_extension="\{\{(.+)\}\} +\{\{\11\}\}( +\{\{\1[[:digit:]]+\}\})*"
      if grep --extended-regexp -- "$consecutive_placeholder_pair_with_broken_numbering_without_extension" "$page" > /dev/null; then
        show_page_warning "$page" placeholder "replace two consequtive placeholders with ellipsis"
        code "$page"

        if [[ ! " $* " =~ " ${FUNCNAME[0]} " ]]; then
          if ! try_confirm "Do you want to fix '$page'?"; then
            ignore "$page"
            continue
          fi
        fi
        
        if sed --in-place --regexp-extended "s/$consecutive_placeholder_pair_with_broken_numbering_without_extension/\{\{\11 \12 ...\}\}/g" "$page"; then
          echo "Done."
        else
          echo "Failed: check whether file can be overridden."
        fi
      fi

      consecutive_placeholder_pair_with_numbering_with_extension="\{\{(.+)1\}\}\.([^ ]+) +\{\{\12\}\}\.\2( +\{\{\1[[:digit:]]+\}\}\.\2)*"
      if grep --extended-regexp -- "$consecutive_placeholder_pair_with_numbering_with_extension" "$page" > /dev/null; then
        show_page_warning "$page" placeholder "replace two consequtive placeholders with extensions with ellipsis"
        code "$page"

        if [[ ! " $* " =~ " ${FUNCNAME[0]} " ]]; then
          if ! try_confirm "Do you want to fix '$page'?"; then
            ignore "$page"
            continue
          fi
        fi
        
        if sed --in-place --regexp-extended "s/$consecutive_placeholder_pair_with_numbering_with_extension/\{\{\11.\2 \12.\2 ...\}\}/g" "$page"; then
          echo "Done."
        else
          echo "Failed: check whether file can be overridden."
        fi
      fi

      consecutive_placeholder_pair_with_broken_numbering_with_extension="\{\{(.+)\}\}\.([^ ]+) +\{\{\12\}\}\.\2( +\{\{\1[[:digit:]]+\}\}\.\2)*"
      if grep --extended-regexp -- "$consecutive_placeholder_pair_with_broken_numbering_with_extension" "$page" > /dev/null; then
        show_page_warning "$page" placeholder "replace two consequtive placeholders with extensions with ellipsis"
        code "$page"

        if [[ ! " $* " =~ " ${FUNCNAME[0]} " ]]; then
          if ! try_confirm "Do you want to fix '$page'?"; then
            ignore "$page"
            continue
          fi
        fi
        
        if sed --in-place --regexp-extended "s/$consecutive_placeholder_pair_with_broken_numbering_with_extension/\{\{\11.\2 \12.\2 ...\}\}/g" "$page"; then
          echo "Done."
        else
          echo "Failed: check whether file can be overridden."
        fi
      fi

      consecutive_placeholder_pair_with_broken_numbering_with_extension="\{\{(.+)\}\}\.([^ ]+) +\{\{\11\}\}\.\2( +\{\{\1[[:digit:]]+\}\}\.\2)*"
      if grep --extended-regexp -- "$consecutive_placeholder_pair_with_broken_numbering_with_extension" "$page" > /dev/null; then
        show_page_warning "$page" placeholder "replace two consequtive placeholders with extensions with ellipsis"
        code "$page"

        if [[ ! " $* " =~ " ${FUNCNAME[0]} " ]]; then
          if ! try_confirm "Do you want to fix '$page'?"; then
            ignore "$page"
            continue
          fi
        fi
        
        if sed --in-place --regexp-extended "s/$consecutive_placeholder_pair_with_broken_numbering_with_extension/\{\{\11.\2 \12.\2 ...\}\}/g" "$page"; then
          echo "Done."
        else
          echo "Failed: check whether file can be overridden."
        fi
      fi
    done
  done
}


declare -i HELP_INFO=1
declare -i WRONG_DIRECTORY_ERROR=1
declare -i WRONG_ARGUMENT_ERROR=1 

declare apply_description_fixes=true
declare apply_placeholder_fixes=true
declare apply_quiet_fixes=true
declare apply_nonquiet_fixes=true

declare -a automatically_applicable_fixes_actions=()

while [[ -n $1 ]]; do
  declare option="$1"
  declare value="$2"

  case "$option" in
    -ncf|--no-confirmation-for)
      if [[ ! -v FUNCTION_ASSOCIATIONS[$value] ]]; then
        show_argument_error "$option" option "replace value with one of: ${!FUNCTION_ASSOCIATIONS[*]}"
        exit $WRONG_ARGUMENT_ERROR
      fi

      automatically_applicable_fixes_actions+=("${FUNCTION_ASSOCIATIONS[$value]}")
      shift
    ;;
    -nd|--no-description)
      apply_description_fixes=false
    ;;
    -np|--no-placeholder)
      apply_placeholder_fixes=false
    ;;
    -nq|--no-quiet)
      apply_quiet_fixes=false
    ;;
    -nnq|--no-non-quiet)
      apply_nonquiet_fixes=false
    ;;
    -h|--help)
      help
      exit $HELP_INFO
    ;;
    -v|--version)
      version 
      exit $HELP_INFO
    ;;
    *)
      show_argument_error "$option" option "remove option"
      exit "$WRONG_ARGUMENT_ERROR"
    ;;
  esac
  shift
done

shopt -s globstar
cd ../pages || {
  echo "Script must be run from the directory where '../pages' subdirectory exists." >&2
  exit $WRONG_DIRECTORY_ERROR
}


are_description_fixes_applicable() {
  [[ $apply_description_fixes == true ]]
}

are_placeholder_fixes_applicable() {
  [[ $apply_placeholder_fixes == true ]]
}

are_quiet_fixes_applicable() {
  [[ $apply_quiet_fixes == true ]]
}

are_nonquiet_fixes_applicable() {
  [[ $apply_nonquiet_fixes == true ]]
}


# Actions without confirmation
are_quiet_fixes_applicable && {
  are_description_fixes_applicable && {
    echo "Fixing stream names in code descriptions..."
    fix_io_stream_names_action "${automatically_applicable_fixes_actions[@]}"
    echo "Fixing 'See also' links in descriptions..."
    fix_see_also_links_action "${automatically_applicable_fixes_actions[@]}"
  }
  are_placeholder_fixes_applicable && {
    echo "Fixing generic file placeholders in code examples..."
    fix_generic_file_placeholders_action "${automatically_applicable_fixes_actions[@]}"
    echo "Fixing generic directory placeholders in code examples..."
    fix_generic_directory_placeholders_action "${automatically_applicable_fixes_actions[@]}"
    echo "Fixing generic file placeholder quoting in code examples..."
    fix_generic_file_placeholder_quoting_action "${automatically_applicable_fixes_actions[@]}"
    echo "Fixing generic directory placeholder quoting in code examples..."
    fix_generic_directory_placeholder_quoting_action "${automatically_applicable_fixes_actions[@]}"
    echo "Fixing number placeholder quoting in code examples..."
    fix_number_placeholder_quoting_action "${automatically_applicable_fixes_actions[@]}"
  }
}

are_nonquiet_fixes_applicable && {
  # Actions with confirmation and ignore file
  echo "Trying to initialize new '$IGNORE_FILE'..."
  try_create_ignore_file
  are_placeholder_fixes_applicable && {
    echo "Fixing file placeholders in code examples..."
    fix_file_placeholders_action "${automatically_applicable_fixes_actions[@]}"
    echo "Fixing ellipsis usage in code examples..."
    fix_placeholder_ellipsis_action "${automatically_applicable_fixes_actions[@]}"
  }
}
