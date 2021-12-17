# chsh

> Change the user's login shell.
> More information: <https://manned.org/chsh>.

- Change the current user's login shell interactively:

`chsh`

- Change the current user's login shell:

`chsh {{/path/to/shell}}`

- Change the login shell for a given user to Zsh:

`chsh --shell {{/path/to/shell}} {{username}}`

- List available shells:

`chsh --list-shells`
