# git restore

> Restore working tree files. Requires Git version 2.23+.
> See also `git checkout` and `git reset`.
> More information: <https://git-scm.com/docs/git-restore>.

- Restore an unstaged file to the version of the current commit (HEAD):

`git restore {{path/to/file}}`

- Restore an unstaged file to the version of a specific commit:

`git restore --source {{commit}} {{path/to/file}}`

- Discard all unstaged changes to tracked files:

`git restore :/`

- Unstage a file:

`git restore --staged {{path/to/file}}`

- Unstage all files:

`git restore --staged :/`

- Discard all changes to files, both staged and unstaged:

`git restore --worktree --staged :/`

- Interactively select sections of files to restore:

`git restore --patch`
