# poetry remove

> Remove a dependency from a Poetry project.
> More information: <https://python-poetry.org/docs/cli/#remove>.

- Remove a package from dependencies:

`poetry remove {{package_name}}`

- Remove a development dependency:

`poetry remove --group {{dev}} {{package_name}}`

- Remove multiple packages:

`poetry remove {{package1}} {{package2}}`

- Remove a package without updating the lock file:

`poetry remove {{package_name}} --lock`

- Remove a package in dry-run mode (show what would be removed):

`poetry remove {{package_name}} --dry-run`

- Display help:

`poetry remove --help`
