# ksh

> Korn Shell, a Bash-compatible command-line interpreter.
> See also: `histexpand` (history expansion).
> More information: <http://kornshell.com>.

- Start an interactive shell session:

`ksh`

- Execute specific [c]ommands:

`ksh -c "{{echo 'ksh is executed'}}"`

- Execute a specific script:

`ksh {{path/to/script.ksh}}`

- Check a specific script for syntax errors:

`ksh -n {{path/to/script.ksh}}`

- Execute a specific script while printing each command before executing it:

`ksh -x {{path/to/script.ksh}}`
