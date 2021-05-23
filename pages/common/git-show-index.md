# git show-index

> Show the packed archive index.
> More information: <https://git-scm.com/docs/git-show-index>.

- Read the `.idx` file for a Git packfile and dump its contents to stdout:

`git show-index {{path/to/file.idx}}`

- Specify the hash algorithm for the index file (experimental):

`git show-index --object-format={{hash_algorithm}} {{path/to/file}}`
