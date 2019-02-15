# paccache

> A flexible pacman cache cleaning utility.

- Remove all but the 3 most recent package versions from the pacman cache:

`paccache -r`

- Set the number of package versions to keep:

`paccache -rk {{num_versions}}`

- Perform dryrun and show the number of candidate packages:

`paccache -d`

- Move candidate packages to a directory instead of deleting them:

`paccache -m {{directory}}`
