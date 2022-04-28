# git ls-files

> Show information about files in the index and the working tree.
> More information: <https://git-scm.com/docs/git-ls-files>.

- Show deleted files:

`git ls-files --deleted`

- Show modified and deleted files:

`git ls-files --modified`

- Show ignored and untracked files:

`git ls-files --others`

- Show untracked files, not ignored:

`git ls-files --others --exclude-standard`
