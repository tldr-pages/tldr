# shellcheck

> Shell script static analysis tool.
> Check shell scripts for errors, usage of deprecated/insecure features, and bad practices.
> More information: <https://www.shellcheck.net>.

- Check a shell script:

`shellcheck {{path/to/script.sh}}`

- Check a shell script interpreting it as the specified shell dialect (overrides the shebang at the top of the script):

`shellcheck --shell {{sh|bash|dash|ksh}} {{path/to/script.sh}}`

- Ignore one or more error types:

`shellcheck --exclude {{SC1009,SC1073}} {{path/to/script.sh}}`

- Also check any sourced shell scripts:

`shellcheck --check-sourced {{path/to/script.sh}}`

- Display output in the specified format (defaults to `tty`):

`shellcheck --format {{tty|checkstyle|diff|gcc|json|json1|quiet}} {{path/to/script.sh}}`

- Enable one or more optional checks:

`shellcheck --enable={{add-default-case|avoid-nullary-conditions}}`

- List all available optional checks that are disabled by default:

`shellcheck --list-optional`
