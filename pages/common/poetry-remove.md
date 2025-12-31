# poetry remove

> Remove a package from the project dependencies.
> More information: <https://python-poetry.org/docs/cli/#remove>.

- Remove one or more packages from the project's dependencies:

`poetry remove {{package1 package2 ...}}`

- Remove a package from the development dependencies:

`poetry remove {{package}} {{[-D|--dev]}}`

- Remove a package from a specific dependency group:

`poetry remove {{package}} {{[-G|--group]}} {{group_name}}`

- Remove a package without making any changes (dry-run):

`poetry remove {{package}} --dry-run`

- Update the lock file only, without removing the package from the environment:

`poetry remove {{package}} --lock`
