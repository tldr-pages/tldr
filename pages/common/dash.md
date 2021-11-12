# dash

> Debian Almquist Shell, a modern, POSIX-compliant implementation of `sh` (not Bash-compatible).
> More information: <https://manned.org/dash>.

- Start an interactive shell session:

`dash`

- Execute a [c]ommand:

`dash -c "{{command}}"`

- Execute a script:

`dash {{path/to/script.dash}}`

- Check a script for syntax errors:

`dash -n {{path/to/script.dash}}`

- Run commands from a script, printing each command before executing it:

`dash -x {{path/to/script.dash}}`

- Execute commands from a script, stopping at the first error:

`dash -e {{path/to/script.dash}}`

- Read and execute commands from stdin:

`dash -s`

- Print the version:

`dash --version`
