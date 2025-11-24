# git clean

> Remove files not tracked by Git from the working tree.
> More information: <https://git-scm.com/docs/git-clean>.

- Interactively delete untracked files:

`git clean {{[-i|--interactive]}}`

- Show which files would be deleted without actually deleting them:

`git clean {{[-n|--dry-run]}}`

- Immediately force deletion of all untracked files:

`git clean {{[-f|--force]}}`

- Delete untracked [d]irectories:

`git clean {{[-f|--force]}} -d`

- Delete only untracked files matching specific paths or glob patterns:

`git clean {{[-f|--force]}} -- {{path/to/directory}} '{{*.ext}}'`

- Delete untracked files except those matching the given patterns:

`git clean {{[-f|--force]}} {{[-e|--exclude]}} {{'*.ext'}} {{[-e|--exclude]}} {{path/to/directory}}/`

- Delete untracked files and e[x]cluded files (those listed in `.gitignore` and `.git/info/exclude`):

`git clean {{[-f|--force]}} -x`
