# poetry-env

> Manage virtualenvs associated with a Poetry project.
> See also: `asdf`.
> More information: <https://python-poetry.org/docs/cli/#env>.

- Print the command to activate a virtualenv:

`poetry env activate`

- Display information about the current environment (-p or -e will display the environment's path or executable):

`poetry env info {{[-p|--path]}} {{[-e|--executable]}}`

- List all virtualenvs associated with the current project (optionally showing the full path):

`poetry env list --full-path`

- Remove specific or all virtualenvs associated with the current project:

`poetry env remove python {{path/to/executable|environment_name}} | poetry env remove --all`

- Activate or create a virtualenv for the project using the specified python executable:

`poetry env use python {{path/to/executable}}`
