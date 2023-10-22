# ksh

> Korn Shell, a Bash-compatible command-line interpreter.
> See also: `histexpand`.
> More information: <http://kornshell.com>.

- Start an interactive shell session:

`ksh`

- Execute specific [c]ommands:

`ksh -c "{{echo 'ksh is executed'}}"`

- Execute a specific script:

`ksh {{path/to/script.ksh}}`

- Check a specific script for syntax errors without executing it:

`ksh -n {{path/to/script.ksh}}`

- Execute a specific script, printing each command in the script before executing it:

`ksh -x {{path/to/script.ksh}}`
