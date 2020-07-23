# dvc commit

> Record changes to DVC-tracked files in the project.
> More information: <https://dvc.org/doc/command-reference/commit>.

- Commit latest version, for all DVC-tracked files and directories:

`dvc commit`

- Commit latest version, for a given DVC-tracked target:

`dvc commit {{target}}`

- Recursively commit all DVC-tracked files in a directory:

`dvc commit --recursive {{path/to/directory}}`
