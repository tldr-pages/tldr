# poetry check

> Manage Poetry file validation and consistency.
> See also: `asdf`.
> More information: <https://python-poetry.org/docs/cli/#check>.

- Check validation and consistency between `pyproject.toml` and `poetry.lock` for Poetry:

`poetry check`

- Verify that `poetry.lock` exists:

`poetry check --lock`

- Fail if warnings are reported:

`poetry check --strict`
