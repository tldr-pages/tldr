# git mv

> Move or rename files and update the Git index.
> More information: <https://git-scm.com/docs/git-mv>.

- Move a file inside the repo and add the movement to the next commit:

`git mv {{path/to/file}} {{new/path/to/file}}`

- Rename a file or directory and add the renaming to the next commit:

`git mv {{path/to/file_or_directory}} {{path/to/destination}}`

- Overwrite the file or directory in the target path if it exists:

`git mv --force {{path/to/file_or_directory}} {{path/to/destination}}`
