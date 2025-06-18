# uv remove

> Remove dependencies from the project's `pyproject.toml` file.
> More information: <https://docs.astral.sh/uv/reference/cli/#uv-remove>.

- Remove a dependency from the project:

`uv remove {{package}}`

- Remove multiple dependencies:

`uv remove {{package1}} {{package2}}`

- Remove a development dependency:

`uv remove --dev {{package}}`

- Remove a dependency from an optional dependency group:

`uv remove --optional {{extra_name}} {{package}}`

- Remove a dependency from a specific dependency group:

`uv remove --group {{group_name}} {{package}}`

- Remove without syncing the virtual environment:

`uv remove --no-sync {{package}}`
