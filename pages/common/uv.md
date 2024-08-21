# uv

> A fast Python package and project manager.
> Some subcommands such as `uv tool` and `uv python` have their own usage documentation.
> More information: <https://docs.astral.sh/uv/reference/cli>.

- Create a new Python project in the current directory:

`uv init`

- Create a new Python project in a directory with the given name:

`uv init {{project_name}}`

- Add a new package to the project:

`uv add {{package}}`

- Remove a package from the project:

`uv remove {{package}}`

- Run a script in the project's environment:

`uv run {{path/to/script.py}}`

- Run a command in the project's environment:

`uv run {{command}}`

- Update a project's environment from `pyproject.toml`:

`uv sync`

- Create a lock file for the project's dependencies:

`uv lock`
