# chsh

> Change user's login shell.
> Part of `util-linux`.
> More information: <https://manned.org/chsh>.

- Set a specific login shell for the current user interactively:

`sudo chsh`

- Set a specific login [s]hell for the current user:

`sudo chsh --shell {{path/to/shell}}`

- Set a login [s]hell for a specific user:

`sudo chsh --shell {{path/to/shell}} {{username}}`

- [l]ist available shells:

`sudo chsh --list-shells`
