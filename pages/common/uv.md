# uv

> A fast Python package and project manager.
> Some subcommands such as `tool` and `python` have their own usage documentation.
> More information: <https://docs.astral.sh/uv/reference/cli>.

- Create a new Python project in the current directory:

`uv init`

- Create a new Python project at the specified path:

`uv init {{path/to/directory}}`

- Add a new dependency to the project:

`uv add {{package}}`

- Remove a dependency from the project:

`uv remove {{package}}`

- Run a script in the project's environment:

`uv run {{path/to/script.py}}`

- Run a command in the project's environment:

`uv run {{command}}`

- Update a project's environment from `pyproject.toml`:

`uv sync`

- Create a lock file for the project's dependencies:

`uv lock`
