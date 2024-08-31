# git clean

> Remove files not tracked by Git from the working tree.
> More information: <https://git-scm.com/docs/git-clean>.

- Delete untracked files:

`git clean`

- [i]nteractively delete untracked files:

`git clean {{--interactive|-i}}`

- Show which files would be deleted without actually deleting them:

`git clean --dry-run`

- Forcefully delete untracked files:

`git clean {{--force|-f}}`

- Forcefully delete untracked [d]irectories:

`git clean {{--force|-f}} -d`

- Delete untracked files, including e[x]cluded files (files ignored in `.gitignore` and `.git/info/exclude`):

`git clean -x`
