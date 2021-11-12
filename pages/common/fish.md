# fish

> The Friendly Interactive SHell, a command-line interpreter designed to be user friendly.
> More information: <https://fishshell.com>.

- Start an interactive shell session:

`fish`

- Start an interactive shell session without loading startup configs:

`fish -N`

- Execute a [c]ommand:

`fish -c "{{command}}"`

- Execute a script:

`fish {{path/to/script.fish}}`

- Check a script for syntax errors but [n]ot execute it:

`fish -n {{path/to/script.fish}}`

- Start an interactive shell session in [p]rivate mode, where the shell does not access old history or save new history:

`fish -P`

- Print the version:

`fish -v`
