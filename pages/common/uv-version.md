# uv version

> Read or update a project's version.
> More information: <https://docs.astral.sh/uv/reference/cli/#uv-version>.

- Display the current project version:

`uv version`

- Set the project version to a specific value:

`uv version {{1.2.3}}`

- Bump the project version using semantic versioning:

`uv version --bump {{major|minor|patch}}`

- Preview version changes without writing to `pyproject.toml`:

`uv version --bump {{patch}} --dry-run`

- Update version for a specific package in a workspace:

`uv version --package {{package_name}} {{1.2.3}}`

- Display version in JSON format:

`uv version --output-format json`
