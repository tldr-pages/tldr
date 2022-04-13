# chsh

> Change a user's login shell.
> More information: <https://manned.org/chsh>.

- Set a specific login shell for a current user interactively:

`chsh`

- Set a specific login shell for a current user:

`chsh --shell {{path/to/shell}}`

- Set a login shell for a specific user:

`chsh --shell {{path/to/shell}} {{username}}`

- Print available shells:

`chsh --list-shells`
