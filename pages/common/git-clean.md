# git clean

> Remove untracked files from the working tree.

- Delete files that are not tracked by git:

`git clean`

- Interactively delete files that are not tracked by git:

`git clean -i`

- Shows what files would be deleted without actually deleting them:

`git clean --dry-run`

- Force delete files that are not tracked by git:

`git clean -f`

- Delete untracked files, including ignored files in `.gitignore` and `$GIT_DIR/info/exclude`:

`git clean -x`
