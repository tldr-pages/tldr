# poetry publish

> Publish a Poetry package to a remote repository (PyPI by default).
> More information: <https://python-poetry.org/docs/cli/#publish>.

- Publish the package to PyPI (requires authentication):

`poetry publish`

- Publish to a specific repository configured in `pyproject.toml`:

`poetry publish --repository {{repository_name}}`

- Publish and build the package first:

`poetry publish --build`

- Publish with a specific username and password:

`poetry publish --username {{username}} --password {{password}}`

- Publish in dry-run mode (show what would be published without actually publishing):

`poetry publish --dry-run`

- Display help:

`poetry publish --help`
