# shopt

> Manage Bash shell options: variables (stored in `$BASHOPTS`) that control behavior specific to the Bash shell.
> Generic POSIX shell variables (stored in `$SHELLOPTS`) are managed with the `set` command instead.

- List of all settable options and whether they are set:

`shopt`

- Set an option:

`shopt -s {{option_name}}`

- Unset an option:

`shopt -u {{option_name}}`

- Print a list of all options and their status formatted as runnable `shopt` commands:

`shopt -p`

- Show help for the command:

`help shopt`
