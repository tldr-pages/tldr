# poetry run

> Execute a command in the Poetry virtual environment.
> More information: <https://python-poetry.org/docs/cli/#run>.

- Run a Python script in the virtual environment:

`poetry run python {{script.py}}`

- Run a command in the virtual environment:

`poetry run {{command}}`

- Run pytest in the virtual environment:

`poetry run pytest`

- Run a Python module as a script:

`poetry run python -m {{module_name}}`

- Run a custom script defined in `pyproject.toml`:

`poetry run {{script_name}}`

- Display help:

`poetry run --help`
