# dvc checkout

> Update data files and directories in the workspace based on current DVC-files.
> More information: <https://dvc.org/doc/command-reference/checkout>.

- Checkout to latest version, for all target files and directories:

`dvc checkout`

- Checkout to latest version, for a given target:

`dvc checkout {{target}}`

- Checkout specific version of target from different Git commit/tag/branch:

`git checkout {{commit_hash/tag/branch}} {{target}} && dvc checkout {{target}}`
