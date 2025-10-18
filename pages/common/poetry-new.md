# poetry new

> Create a new Python project with a standard project structure.
> More information: <https://python-poetry.org/docs/cli/#new>.

- Create a new project with the standard layout:

`poetry new {{project_name}}`

- Create a new project with a source layout (src/ directory):

`poetry new {{project_name}} --src`

- Create a new project with a specific name (different from the directory):

`poetry new {{project_name}} --name {{package_name}}`

- Create a new project and include a README file in a specific format:

`poetry new {{project_name}} --readme {{md}}`

- Display help:

`poetry new --help`
