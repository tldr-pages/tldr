# git fast-export

> Exports the contents and history of a Git repository in a streamable, plain-text format.
> More information: <https://manned.org/git-fast-export>.

- Export the Entire Git Repository History to console:

`git fast-export --all`

- Export the entire repository to a file:

`git fast-export --all > {{history.txt}}`

- Export a specific branch only:

`git fast-export {{main}}`

- Export with progress shown:

`git fast-export --progress={{5}} --all > {{repo_progress.export}}`

- Export only a specific subdirectory’s history:

`git fast-export --all -- {{path/to/subdir}} > {{subdir.dat}}`
