# poetry-env

> Manage virtual environments associated with a Poetry project.
> See also: `asdf`.
> More information: <https://python-poetry.org/docs/cli/#env>.

- Print the command to activate a virtual environment:

`poetry env activate`

- Display information about the current environment (`-p` or `-e` will display the environment's path or executable):

`poetry env info {{[-p|--path]}} {{[-e|--executable]}}`

- List all virtual environments associated with the current project (optionally showing the full path):

`poetry env list --full-path`

- Remove specific or all virtual environments associated with the current project:

`poetry env remove python {{path/to/executable|environment_name}} | poetry env remove --all`

- Activate or create a virtual environment for the project using the specified Python executable:

`poetry env use python {{path/to/executable}}`
