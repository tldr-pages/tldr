# git rscp

> Reverse `git scp` - copy files from the working directory of a remote repository to the current working tree.
> Part of `git-extras`.
> More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-scp>.

- Copy specific files from a remote:

`git rscp {{remote_name}} {{path/to/file1 path/to/file2 ...}}`

- Copy a specific directory from a remote:

`git rscp {{remote_name}} {{path/to/directory}}`
