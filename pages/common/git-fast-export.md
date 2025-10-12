# git fast-export

> Export the contents and history of a Git repository in a streamable, plain-text format.
> More information: <https://manned.org/git-fast-export>.

- Export the entire Git repository history to `stdout`:

`git fast-export --all`

- Export the entire repository to a file:

`git fast-export --all > {{path/to/file}}`

- Export a specific branch only:

`git fast-export {{main}}`

- Export with `progress` statements every `n` objects (for showing progress during `git fast-import`):

`git fast-export --progress {{n}} --all > {{path/to/file}}`

- Export only a specific subdirectory's history:

`git fast-export --all -- {{path/to/directory}} > {{path/to/file}}`
