# poetry version

> Manage Poetry project version.
> Assumes the following project stages: `patch`, `minor`, `major`, `prepatch`, `preminor`, `premajor`, `prerelease`.
> See also: `asdf`.
> More information: <https://python-poetry.org/docs/cli/#version>.

- Output the current version:

`poetry version {{[-s|--short]}}`

- Set project to a specific phase:

`poetry version {{stage}}`

- Increment the project to the next prerelease phase:

`poetry version --next-phase`

- Test project stage function without writing to `pyproject.toml`:

`poetry version {{stage}} --dry-run`
