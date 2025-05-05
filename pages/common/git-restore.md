# git restore

> Restore working tree files. Requires Git version 2.23+.
> See also `git checkout` and `git reset`.
> More information: <https://git-scm.com/docs/git-restore>.

- Restore an unstaged file to the staged version:

`git restore {{path/to/file}}`

- Restore an unstaged file to the version of a specific commit:

`git restore {{[-s|--source]}} {{commit}} {{path/to/file}}`

- Discard all unstaged changes to tracked files:

`git restore :/`

- Unstage a file:

`git restore {{[-S|--staged]}} {{path/to/file}}`

- Unstage all files:

`git restore {{[-S|--staged]}} :/`

- Discard all changes to files, both staged and unstaged:

`git restore {{[-W|--worktree]}} {{[-S|--staged]}} :/`

- Interactively select sections of files to restore:

`git restore {{[-p|--patch]}}`
