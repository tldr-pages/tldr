# poetry new

> Create a new Poetry project in a specific directory.
> More information: <https://python-poetry.org/docs/cli/#new>.

- Create a new project (defaults to `src` layout):

`poetry new {{path/to/directory}}`

- Create a new project asking for configuration details interactively:

`poetry new {{path/to/directory}} {{[-i|--interactive]}}`

- Create a new project with a specific package name:

`poetry new {{path/to/directory}} --name {{package_name}}`

- Create a new project using the flat layout (without the `src` directory):

`poetry new {{path/to/directory}} --flat`

- Create a new project with a specific author:

`poetry new {{path/to/directory}} --author "{{Name <email@example.com>}}"`

- Create a new project with a specific README format:

`poetry new {{path/to/directory}} --readme {{md|rst|txt|...}}`
