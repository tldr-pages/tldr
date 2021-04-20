# dash

> Debian Almquist Shell, a modern, POSIX-compliant implementation of `sh` (not Bash-compatible).
> More information: <https://manned.org/dash>.

- Start an interactive shell session:

`dash`

- Execute a command and then exit:

`dash -c "{{command}}"`

- Execute a script:

`dash {{path/to/script.sh}}`

- Run commands from a script, printing each command before executing it:

`dash -x {{path/to/script.sh}}`

- Execute commands from a script, stopping at the first error:

`dash -e {{path/to/script.sh}}`

- Read and execute commands from stdin:

`dash -s`
