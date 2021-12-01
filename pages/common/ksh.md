# ksh

> Korn Shell, a Bash-compatible command-line interpreter.
> See also `histexpand` for history expansion.
> More information: <http://kornshell.com>.

- Start an interactive shell session:

`ksh`

- Execute [c]ommands:

`ksh -c "echo 'ksh is executed'"`

- Execute a script:

`ksh {{path/to/script.ksh}}`

- Check a script for syntax errors:

`ksh -n {{path/to/script.ksh}}`

- Execute a script while printing each command before executing it:

`ksh -x {{path/to/script.ksh}}`

- Print the version (`$KSH_VERSION` contains the version without the license information):

`ksh --version`
