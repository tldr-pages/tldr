# dash

> Debian Almquist Shell, a modern, POSIX-compliant implementation of `sh` (not Bash-compatible).
> More information: <https://manned.org/dash>.

- Start an interactive shell session:

`dash`

- Execute specific [c]ommands:

`dash -c "{{echo 'dash is executed'}}"`

- Execute a specific script:

`dash {{path/to/script.sh}}`

- Check a specific script for syntax errors:

`dash -n {{path/to/script.sh}}`

- Execute a specific script while printing each command before executing it:

`dash -x {{path/to/script.sh}}`

- Execute a specific script and stop at the first [e]rror:

`dash -e {{path/to/script.sh}}`

- Execute specific commands from `stdin`:

`{{echo "echo 'dash is executed'"}} | dash`
