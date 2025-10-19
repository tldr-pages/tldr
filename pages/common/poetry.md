# poetry

> Python dependency and package manager.
> Create projects, manage dependencies/virtual environments, build and publish packages.
> More information: <https://python-poetry.org/docs/cli/>.

- Create a new project in a directory:

`poetry new {{project_name}}`

- Initialize Poetry in the current directory (interactive):

`poetry init`

- Add a runtime dependency:

`poetry add {{package}}`

- Add a dependency to a specific group (for example, "dev"):

`poetry add --group {{dev}} {{package}}`

- Install dependencies from `pyproject.toml` / `poetry.lock`:

`poetry install`

- Run a command inside the project's virtual environment:

`poetry run {{command}}`

- Update all dependencies to the latest allowed versions:

`poetry update`

- Build a source distribution and a wheel:

`poetry build`
