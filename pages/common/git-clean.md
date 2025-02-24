# git clean

> Remove files not tracked by Git from the working tree.
> More information: <https://git-scm.com/docs/git-clean>.

- Delete untracked files:

`git clean`

- Interactively delete untracked files:

`git clean {{[-i|--interactive]}}`

- Show which files would be deleted without actually deleting them:

`git clean {{[-n|--dry-run]}}`

- Forcefully delete untracked files:

`git clean {{[-f|--force]}}`

- Forcefully delete untracked [d]irectories:

`git clean {{[-f|--force]}} -d`

- Delete untracked files, including e[x]cluded files (files ignored in `.gitignore` and `.git/info/exclude`):

`git clean -x`
