# dvc checkout

> Checkout data files and directories from cache.
> More information: <https://doc.dvc.org/command-reference/checkout>.

- Check out the latest version of all target files and directories:

`dvc checkout`

- Check out the latest version of a specified target:

`dvc checkout {{target}}`

- Check out a specific version of a target from a different Git commit/tag/branch:

`git checkout {{commit_hash|tag|branch}} {{target}} && dvc checkout {{target}}`
