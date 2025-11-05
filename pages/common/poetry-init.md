# poetry init

> Create a basic `pyproject.toml` file interactively.
> More information: <https://python-poetry.org/docs/cli/#init>.

- Create a `pyproject.toml` file interactively:

`poetry init`

- Create a `pyproject.toml` file with prefilled values:

`poetry init --name {{package_name}} --author "{{author_name <email@example.com>}}"`

- Create a `pyproject.toml` file without interaction (using defaults):

`poetry init {{[-i|--no-interaction]}}`

- Create a `pyproject.toml` file and add a dependency:

`poetry init --dependency {{package_name}}`

- Create a `pyproject.toml` file and add a development dependency:

`poetry init --dev-dependency {{package_name}}`

- Display help:

`poetry init {{[-h|--help]}}`
