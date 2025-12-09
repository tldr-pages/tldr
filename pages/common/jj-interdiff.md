# jj interdiff

> Compare changes of two revisions.
> More information: <https://jj-vcs.github.io/jj/latest/cli-reference/#jj-interdiff>.

- Compare changes from a revision to the working copy:

`jj interdiff {{[-f|--from]}} {{revset}}`

- Compare changes from a revision to another revision:

`jj interdiff {{[-f|--from]}} {{from_revset}} {{[-t|--to]}} {{to_revset}}`

- Compare changes in specific paths only:

`jj interdiff {{[-f|--from]}} {{from_revset}} {{[-t|--to]}} {{to_revset}} {{filesets}}`

- Show a summary of changes:

`jj interdiff {{[-f|--from]}} {{revset}} {{[-s|--summary]}}`

- Show diff statistics:

`jj interdiff {{[-f|--from]}} {{revset}} --stat`

- Show a Git-format diff:

`jj interdiff {{[-f|--from]}} {{revset}} --git`

- Show a word-level diff with changes indicated only by color:

`jj interdiff {{[-f|--from]}} {{revset}} --color-words`
