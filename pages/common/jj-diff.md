# jj diff

> Compare file contents between two revisions.
> More information: <https://jj-vcs.github.io/jj/latest/cli-reference/#jj-diff>.

- Show changes of current revision:

`jj diff`

- Show changes of given revsets (e.g. `B::D`, `A..D`, `B|C|D`, etc.):

`jj diff {{[-r|--revisions]}} {{revsets}}`

- Show changes from given revision to given revision:

`jj diff {{[-f|--from]}} {{from_revset}} {{[-t|--to]}} {{to_revset}}`

- Show diff statistics:

`jj diff --stat`

- Show a Git-format diff:

`jj diff --git`
