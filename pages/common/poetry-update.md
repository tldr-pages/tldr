# poetry update

> Update the dependencies as according to the `pyproject.toml` file.
> More information: <https://python-poetry.org/docs/cli/#update>.

- Update all dependencies:

`poetry update`

- Update one or more specific packages:

`poetry update {{package1 package2 ...}}`

- Update the lock file only, without installing the packages:

`poetry update --lock`

- Synchronize the environment with the locked packages:

`poetry update --sync`

- Update dependencies only for a specific group:

`poetry update --only {{group_name}}`

- Simulate the update process without making changes:

`poetry update --dry-run`
