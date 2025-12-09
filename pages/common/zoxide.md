# zoxide

> Keep track of the most frequently used directories.
> Uses a ranking algorithm to navigate to the best match.
> More information: <https://manned.org/zoxide>.

- Go to the highest-ranked directory that contains `string` in the name:

`zoxide query string`

- Go to the highest-ranked directory that contains `string1` and then `string2`:

`zoxide query string1 string2`

- Start an interactive directory search (requires `fzf`):

`zoxide query {{[-i|--interactive]}}`

- Add a directory or increment its rank:

`zoxide add {{path/to/directory}}`

- Remove a directory from `zoxide`'s database:

`zoxide remove {{path/to/directory}}`

- Generate shell configuration for command aliases (`z`, `zi`):

`zoxide init {{bash|elvish|fish|nushell|posix|powershell|tcsh|xonsh|zsh}}`
