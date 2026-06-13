# uv export

> Export the project's lockfile to an alternate format.
> More information: <https://docs.astral.sh/uv/reference/cli/#uv-export>.

- Export dependencies to a `requirements.txt` file:

`uv export --format requirements-txt {{[-o|--output-file]}} {{requirements.txt}}`

- Export dependencies to `pylock.toml` format:

`uv export --format pylock.toml`

- Export only production dependencies (exclude dev dependencies):

`uv export --no-dev`

- Export including a specific optional dependency group:

`uv export --extra {{group_name}}`

- Export including all optional dependencies:

`uv export --all-extras`

- Export including a specific dependency group:

`uv export --group {{group_name}}`

- Export without hashes:

`uv export --no-hashes`

- Export dependencies for a specific package in the workspace:

`uv export --package {{package_name}}`
