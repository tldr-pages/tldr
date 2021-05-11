# git show-index

> Show packed archive index.
> More information: <https://git-scm.com/docs/git-show-index>.

- Reads the '.idx' file for a Git packfile and dump it's contents (stdout):

`git show-index {{path/to/file}}`

- Specify the hash algorithm for the index file (experimental):

`git show-index --object-format={{hash_algorithm}} {{path/to/file}}`
