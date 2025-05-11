# git ls-files

> Show information about files in the index and the working tree.
> More information: <https://git-scm.com/docs/git-ls-files>.

- Show deleted files:

`git ls-files {{[-d|--deleted]}}`

- Show modified and deleted files:

`git ls-files {{[-m|--modified]}}`

- Show ignored and untracked files:

`git ls-files {{[-o|--others]}}`

- Show untracked files, not ignored:

`git ls-files {{[-o|--others]}} --exclude-standard`
