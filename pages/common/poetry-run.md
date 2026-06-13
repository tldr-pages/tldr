# poetry run

> Run a command in the project's virtual environment.
> More information: <https://python-poetry.org/docs/cli/#run>.

- Run a command inside the virtual environment:

`poetry run {{command}}`

- Run a command with arguments:

`poetry run {{command}} {{argument1 argument2 ...}}`

- Run a script defined in `pyproject.toml`:

`poetry run {{script_name}}`

- Run a Python script:

`poetry run python {{path/to/script.py}}`
