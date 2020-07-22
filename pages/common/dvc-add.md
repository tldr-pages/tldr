# dvc add

> Adds changed files to the index.
> More information: <https://dvc.org/doc/command-reference/add>.

- Add a single target file to the index:

`dvc add {{path/to/file}}`

- Add target directory to the index:

`dvc add {{path/to/directory}}`

- Recursively add all files in target directory:

`dvc add --recursive {{path/to/directory}}`

- Add target file with custom .dvc file name

`dvc add --file custom_name.dvc {{path/to/file}}`
