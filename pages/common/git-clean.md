# git clean

> Remove untracked files from the working tree.
> More information: <https://git-scm.com/docs/git-clean>.

- Delete files that are not tracked by git:

`git clean`

- Interactively delete files that are not tracked by git:

`git clean -i`

- Show what files would be deleted without actually deleting them:

`git clean --dry-run`

- Forcefully delete files that are not tracked by git:

`git clean -f`

- Forcefully delete directories that are not tracked by git:

`git clean -fd`

- Delete untracked files, including ignored files in `.gitignore` and `.git/info/exclude`:

`git clean -x`
