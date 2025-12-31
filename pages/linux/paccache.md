# paccache

> A `pacman` cache cleaning utility.
> More information: <https://manned.org/paccache>.

- Remove all but the 3 most recent package versions from the `pacman` cache:

`paccache {{[-r|--remove]}}`

- Set the number of package versions to keep:

`paccache {{[-rk|--remove --keep]}} {{num_versions}}`

- Perform a dry-run and show the number of candidate packages for deletion:

`paccache {{[-d|--dryrun]}}`

- Move candidate packages to a directory instead of deleting them:

`paccache {{[-m|--move]}} {{path/to/directory}}`
