# git clean

> Remove files not tracked by Git from the working tree.
> More information: <https://git-scm.com/docs/git-clean>.

- Delete untracked files:

`git clean`

- [i]nteractively delete untracked files:

`git clean -i`

- Show which files would be deleted without actually deleting them:

`git clean --dry-run`

- [f]orcefully delete untracked files:

`git clean -f`

- [f]orcefully delete untracked [d]irectories:

`git clean -fd`

- Delete untracked files, including e[x]cluded files (files ignored in `.gitignore` and `.git/info/exclude`):

`git clean -x`
