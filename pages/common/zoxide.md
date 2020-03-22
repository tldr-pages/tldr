# zoxide

> Keep track of the most frequently used directories.
> Uses a ranking algorithm to navigate to the best match.
> More information: <https://github.com/ajeetdsouza/zoxide>.

- Go to the highest-ranked directory that contains "foo" in the name:

`zoxide query {{foo}}`

- Go to the highest-ranked directory that contains "foo" and then "bar":

`zoxide query {{foo}} {{bar}}`

- Start an interactive directory search (requires `fzf`):

`zoxide query --interactive`

- Add a directory or increment its rank:

`zoxide add {{path/to/dir}}`

- Remove a directory from `zoxide`'s database:

`zoxide remove {{path/to/dir}}`

- Generate shell configuration for command aliases (`z`, `za`, `zi`, `zq`, `zr`):

`zoxide init {{bash|fish|zsh}}`
