# git mv

> Move or rename files and update the git index.
> More information: <https://git-scm.com/docs/git-mv>.

- Move file inside the repo and add the movement to the next commit:

`git mv {{path/to/file}} {{new/path/to/file}}`

- Rename file and add renaming to the next commit:

`git mv {{filename}} {{new_filename}}`

- Overwrite the file in the target path if it exists:

`git mv --force {{file}} {{target}}`
