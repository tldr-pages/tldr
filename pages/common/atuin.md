# atuin

> Store your shell history in a searchable database.
> Optionally sync your encrypted history between machines.
> More information: <https://docs.atuin.sh/>.

- Install atuin into your shell:

`eval "$(atuin init {{bash|zsh|fish}})"`

- Import history from the shell default history file:

`atuin import auto`

- Search shell history for a specific command:

`atuin search {{command}}`

- Register an account on the default sync server using the specified username, email and password:

`atuin register {{[-u|--username]}} {{username}} {{[-e|--email]}} {{email}} {{[-p|--password]}} {{password}}`

- Login to the default sync server:

`atuin login {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}}`

- Sync history with the sync server:

`atuin sync`
