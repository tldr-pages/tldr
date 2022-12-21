#!/usr/bin/env bash

[[ ! -v SUCCESS ]] && declare -i -r SUCCESS=0
[[ ! -v FAILURE ]] && declare -i -r FAILURE=1
[[ ! -v FAILURE_WITH_INVALID_OPTION ]] && declare -i -r FAILURE_WITH_INVALID_OPTION=1
[[ ! -v FAILURE_WITH_INVALID_ARGUMENT ]] && declare -i -r FAILURE_WITH_INVALID_ARGUMENT=1
[[ ! -v FAILURE_WITH_INVALID_ARGUMENT_ASSIGNMENT ]] && declare -i -r FAILURE_WITH_INVALID_ARGUMENT_ASSIGNMENT=1
[[ ! -v FAILURE_WITH_INVALID_ARGUMENT_OUT_OF_RANGE ]] && declare -i -r FAILURE_WITH_INVALID_ARGUMENT_OUT_OF_RANGE=1

[[ ! -v TRUE ]] && declare -i -r TRUE=$SUCCESS
[[ ! -v FALSE ]] && declare -i -r FALSE=$FAIL


true() {
  echo 0
  builtin true
}

false() {
  echo 1
  builtin false
}


function_name() {
  echo -n "${FUNCNAME[1]}"
}

caller_function_name() {
  echo -n "${FUNCNAME[2]}"
}

__core_function_failure_with_invalid_option_error() {
  echo "${1:-$(caller_function_name)}: wrong option passed, or too few or much options passed" >&2
}

__core_function_failure_with_invalid_argument_error() {
  echo "${1:-$(caller_function_name)}: wrong argument passed, or too few or much arguments passed" >&2
}

__core_function_failure_with_invalid_argument_assignment_error() {
  echo "${1:-$(caller_function_name)}: wrong argument assignment passed" >&2
}

__core_function_failure_with_invalid_argument_out_of_range_error() {
  if (( $# == 0 )); then
    echo "${1:-$(caller_function_name)}: wrong argument passed" >&2
  else
    echo "${1:-$(caller_function_name)}: wrong argument passed, expected one of: $*" >&2
  fi
}

__core_function_info() {
  [[ -n "$3" ]] && {
    __core_function_failure_with_invalid_argument_error "$2"
    return $FAILURE_WITH_INVALID_ARGUMENT
  }

  declare description="$1"

  echo "$(function_name): $(caller_function_name): $description"
}

__core_function_warn() {
  [[ -n "$3" ]] && {
    __core_function_failure_with_invalid_argument_error "$2"
    return $FAILURE_WITH_INVALID_ARGUMENT
  }

  declare description="$1"

  echo "$(function_name): $(caller_function_name): $description"
}

__core_function_error() {
  [[ -n "$3" ]] && {
    __core_function_failure_with_invalid_argument_error "$2"
    return $FAILURE_WITH_INVALID_ARGUMENT
  }

  declare description="$1"

  echo "$(function_name): $(caller_function_name): $description"
}


raw_foreground() {
  [[ -n "$2" ]] && {
    __core_function_failure_with_invalid_argument_error
    return $FAILURE_WITH_INVALID_ARGUMENT
  }

  declare color_name="$1"
  declare -A color_name_associations=(
    [none]=0
    [black]=30
    [red]=31
    [green]=32
    [yellow]=33
    [blue]=34
    [magenta]=35
    [cyan]=36
    [light-gray]=37
    [gray]=90
    [light-red]=91
    [light-green]=92
    [light-yellow]=93
    [light-blue]=94
    [light-magenta]=95
    [light-cyan]=96
    [white]=97
  )

  [[ ! -v color_name_associations[$color_name] ]] && {
    __core_function_failure_with_invalid_argument_out_of_range_error "${!color_name_associations[@]}"
    return $FAILURE_WITH_INVALID_ARGUMENT_OUT_OF_RANGE
  }
  echo -n "\e[${color_name_associations[$color_name]}m"
}

raw_background() {
  [[ -n "$2" ]] && {
    __core_function_failure_with_invalid_argument_error
    return $FAILURE_WITH_INVALID_ARGUMENT
  }

  declare -A color_name_associations=(
    [none]=0
    [black]=40
    [red]=41
    [green]=42
    [yellow]=43
    [blue]=44
    [magenta]=45
    [cyan]=46
    [light-gray]=47
    [gray]=100
    [light-red]=101
    [light-green]=102
    [light-yellow]=103
    [light-blue]=104
    [light-magenta]=105
    [light-cyan]=106
    [white]=107
  )

  declare color_name="$1"

  [[ ! -v color_name_associations[$color_name] ]] && {
    __core_function_failure_with_invalid_argument_out_of_range_error "${!color_name_associations[@]}"
    return $FAILURE_WITH_INVALID_ARGUMENT_OUT_OF_RANGE
  }
  echo -n "\e[${color_name_associations[$color_name]}m"
}

foreground() {
  declare raw_color
  raw_color="$(raw_foreground "$1")" || exit $?
  echo -e "$raw_color"
}

background() {
  declare raw_color
  raw_color="$(raw_background "$1")" || exit $?
  echo -e "$raw_color"
}


colorize() {
  [[ -n "$2" ]] && {
    __core_function_failure_with_invalid_argument_error
    return $FAILURE_WITH_INVALID_ARGUMENT
  }

  declare output=" $1 "
  output=${output// true / $(raw_foreground cyan)true$(raw_foreground none) }
  output=${output// false / $(raw_foreground cyan)false$(raw_foreground none) }
  output=${output//\'/$(raw_foreground yellow)\'$(raw_foreground none)}
  output=${output//\"/$(raw_foreground yellow)\"$(raw_foreground none)}

  echo -n "${output:1:${#output} - 2}"
}

info() {
  declare arguments=("$@")
  declare output
  output="$(__core_function_info "${arguments[0]}" "info" "${arguments[@]:2}" 2>&1)"
  if (( $? != 0 )); then
    echo "$output"
    if [[ $output == *"too few or much"* ]]; then
      exit $FAILURE_WITH_INVALID_ARGUMENT
    else
      exit $FAILURE_WITH_INVALID_ARGUMENT_OUT_OF_RANGE
    fi
  fi

  output=${output/__core_function_info/$(raw_foreground magenta)$(caller_function_name)$(raw_foreground none)}
  output=${output//:/$(raw_foreground red):$(raw_foreground none)}
  output=${output/ info/ $(raw_foreground "$INFO_FOREGROUND_COLOR")$(raw_background "$INFO_BACKGROUND_COLOR")info$(raw_foreground none)}
  output="$(colorize "$output")"
  echo -e "$output"
}

warn() {
  declare arguments=("$@")
  declare output
  output="$(__core_function_warn "${arguments[0]}" "warn" "${arguments[@]:2}" 2>&1)"
  if (( $? != 0 )); then
    echo "$output"
    if [[ $output == *"too few or much"* ]]; then
      exit $FAILURE_WITH_INVALID_ARGUMENT
    else
      exit $FAILURE_WITH_INVALID_ARGUMENT_OUT_OF_RANGE
    fi
  fi

  output=${output/__core_function_warn/$(raw_foreground magenta)$(caller_function_name)$(raw_foreground none)}
  output=${output//:/$(raw_foreground red):$(raw_foreground none)}
  output=${output/ warn/ $(raw_foreground "$WARN_FOREGROUND_COLOR")$(raw_background "$WARN_BACKGROUND_COLOR")warn$(raw_foreground none)}
  output="$(colorize "$output")"
  echo -e "$output"
}

error() {
  declare arguments=("$@")
  declare output
  output="$(__core_function_error "${arguments[0]}" "error" "${arguments[@]:2}" 2>&1)"
  if (( $? != 0 )); then
    echo "$output"
    if [[ $output == *"too few or much"* ]]; then
      exit $FAILURE_WITH_INVALID_ARGUMENT
    else
      exit $FAILURE_WITH_INVALID_ARGUMENT_OUT_OF_RANGE
    fi
  fi

  output=${output/__core_function_error/$(raw_foreground magenta)$(caller_function_name)$(raw_foreground none)}
  output=${output//:/$(raw_foreground red):$(raw_foreground none)}
  output=${output/ error/ $(raw_foreground "$ERROR_FOREGROUND_COLOR")$(raw_background "$ERROR_BACKGROUND_COLOR")error$(raw_foreground none)}
  output="$(colorize "$output")"
  echo -e "$output"
}

__core_load_default_colors() {
  INFO_FOREGROUND_COLOR="white"
  WARN_FOREGROUND_COLOR="white"
  ERROR_FOREGROUND_COLOR="white"

  INFO_BACKGROUND_COLOR="green"
  WARN_BACKGROUND_COLOR="yellow"
  ERROR_BACKGROUND_COLOR="red"
}

list_page_existing_urls() {
  declare command_name="$1"

  [[ -z "$command_name" ]] && {
    error "command name expected to be passed"
    exit "$FAILURE_WITH_INVALID_ARGUMENT"
  }

  declare base_url="https://manned.org/man"
  declare arch_url="$base_url/arch"
  declare freebsd_url="$base_url/freebsd"

  declare urls=()

  for url in "$arch_url" "$freebsd_url"; do
    declare page_url="$url/$command_name.1"
    info "checking '$page_url' url"
    if wget --spider "$page_url"; then
      urls+=("$url")
    fi
  done

  echo "${urls[*]}"
}

main() {
  __core_load_default_colors
  list_page_existing_urls "cat"
}

main
