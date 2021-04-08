# dash

> Debian Almquist Shell, a modern, POSIX-compliant implementation of `sh` (not `bash`-compatible).
> More information: <https://wiki.archlinux.org/index.php/Dash>.

- Start an interactive shell session:

`dash`

- Execute a command and then exit:

`dash -c "{{command}}"`

- Execute a script file:

`dash {{path/to/script.sh}}`

- Run commands from a file, logging all commands executed to the terminal:

`dash -x {{file.sh}}`
