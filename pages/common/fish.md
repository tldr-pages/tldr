# fish

> The Friendly Interactive SHell.
> A command-line interpreter designed to be user friendly.
> More information: <https://fishshell.com>.

- Start interactive shell:

`fish`

- Execute a command:

`fish -c "{{command}}"`

- Run commands from a file:

`fish {{file.fish}}`

- Check a file for syntax errors:

`fish --no-execute {{file.fish}}`

- Display version information and exit:

`fish --version`

- Set and export environmental variables that persist across restarts:

`set -Ux {{variable_name}} {{variable_value}}`
