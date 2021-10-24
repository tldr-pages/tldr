# git reset

> Undo commits or unstage changes, by resetting the current Git HEAD to the specified state.
> If a path is passed, it works as "unstage"; if a commit hash or branch is passed, it works as "uncommit".
> More information: <https://git-scm.com/docs/git-reset>.

- Unstage everything:

`git reset`

- Unstage specific file(s):

`git reset {{path/to/file(s)}}`

- Interactively unstage portions of a file:

`git reset --patch {{path/to/file}}`

- Undo the last commit, keeping its changes (and any further uncommitted changes) in the filesystem:

`git reset HEAD~`

- Undo the last two commits, adding their changes to the index, i.e. staged for commit:

`git reset --soft HEAD~2`

- Discard any uncommitted changes, staged or not (for only unstaged changes, use `git checkout`):

`git reset --hard`

- Reset the repository to a given commit, discarding committed, staged and uncommitted changes since then:

`git reset --hard {{commit}}`
