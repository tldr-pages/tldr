# dvc checkout

> Update data files and directories in the workspace based on current DVC-files.
> More information: <https://dvc.org/doc/command-reference/checkout>.

- Checkout the latest version of all target files and directories:

`dvc checkout`

- Checkout to latest version of a specified target:

`dvc checkout {{target}}`

- Checkout a specific version of a target from a different Git commit/tag/branch:

`git checkout {{commit_hash|tag|branch}} {{target}} && dvc checkout {{target}}`
