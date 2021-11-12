# fish

> The Friendly Interactive SHell, a command-line interpreter designed to be user friendly.
> More information: <https://fishshell.com>.

- Start an interactive shell session:

`fish`

- Start an interactive shell session in [p]rivate mode, where the shell does not access old history or save new history:

`fish -p`

- Execute a [c]ommand and then exit:

`fish -c "{{command}}"`

- Execute a script and then exit:

`fish {{path/to/script.fish}}`

- Check a script for syntax errors but [n]ot execute it and then exit:

`fish -n {{path/to/script.fish}}`

- Print the Fish version and then exit:

`fish -v`
