# poetry update

> Update dependencies to their latest compatible versions and update the lock file.
> More information: <https://python-poetry.org/docs/cli/#update>.

- Update all dependencies to their latest compatible versions:

`poetry update`

- Update a specific package to its latest compatible version:

`poetry update {{package_name}}`

- Update multiple specific packages:

`poetry update {{package1}} {{package2}}`

- Update all packages without updating the lock file:

`poetry update --lock`

- Update packages in dry-run mode (show what would be updated):

`poetry update --dry-run`

- Display help:

`poetry update --help`
