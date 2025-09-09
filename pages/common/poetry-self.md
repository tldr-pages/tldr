# poetry-self

> Manage the Poetry installation/runtime environment itself.
> These commands reference `pyproject.toml` and `poetry.lock` files in your Poetry configuration directory.
> See also: `asdf`.
> More information: <https://python-poetry.org/docs/cli/#self>.

- Install a package:

`poetry self add {{package_name}}`

- Install dependencies from the Poetry installation's `pyproject.toml` file:

`poetry self install`

- Lock dependencies from the Poetry installation's `pyproject.toml` file:

`poetry self lock`

- Remove a package:

`poetry self remove {{package_name}}`

- List all installed packages:

`poetry self show`

- List all installed plugins:

`poetry self show plugins`

- Sync the runtime environment with the Poetry installation's `poetry.lock` file:

`poetry self sync`

- Update dependencies from the Poetry installation's `pyproject.toml` file:

`poetry self update`
