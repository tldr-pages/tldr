# chsh

> Change user's login shell.
> Part of `util-linux`.
> More information: <https://manned.org/chsh>.

- Set a specific login shell for the current user interactively:

`chsh`

- List available shells:

`chsh {{[-l|--list-shells]}}`

- Set a specific login shell for the current user:

`chsh {{[-s|--shell]}} {{path/to/shell}}`

- Set a login shell for a specific user:

`sudo chsh {{[-s|--shell]}} {{path/to/shell}} {{username}}`
