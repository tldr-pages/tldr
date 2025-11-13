# su

> Switch shell to another user.
> More information: <https://manned.org/su>.

- Switch to superuser (requires the root password):

`su`

- Switch to a given user (requires the user's password):

`su {{username}}`

- Switch to a given user and simulate a full login shell:

`su - {{username}}`

- Execute a command as another user:

`su - {{username}} {{[-c|--command]}} "{{command}}"`

- Switch to a given user and use a specific shell (e.g., zsh, fish, bash):

`su {{[-s|--shell]}} /{{path/to/shell}} {{username}}`

- Display help:

`su {{[-h|--help]}}`

- Display version :

`su {{[-V|--version]}}`

