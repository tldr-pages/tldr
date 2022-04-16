# chsh

> Change the user's login shell.
> More information: <https://manned.org/chsh>.

- Change the current user's login shell interactively:

`chsh`

- Change the login shell of the current user:

`chsh -s {{path/to/shell}}`

- Change the login shell for a given user:

`chsh -s {{path/to/shell}} {{username}}`

- List available shells:

`chsh --list-shells`
