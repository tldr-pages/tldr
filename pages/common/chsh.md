# chsh

> Change a user's login shell.
> More information: <https://manned.org/chsh>.

- Set a specific login shell for the current user interactively:

`chsh`

- Set a specific login shell for the current user:

`chsh -s {{path/to/shell}}`

- Set a login shell for a specific user:

`chsh -s {{path/to/shell}} {{username}}`

- Print available shells:

`chsh --list-shells`
