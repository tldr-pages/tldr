# git scp

> Copy files from the current working tree to the working directory of a remote repository.
> Internally this script uses rsync and not scp as the name suggests.
> Part of `git-extras`.
> More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-scp>.

- Copy unstaged files to remote.:

`git scp staging`

- Copy staged and unstaged files to remote:

`git scp staging HEAD`

- Copy files that has been changed in the last commit, plus any staged or unstaged files to remote:

`git scp staging HEAD~1`

- Copy specific files:

`git scp staging {{path/to/file1}}...{{path/to/filen}}`

- Copy specific directory

`git scp staging {{path/to/directory}}`
