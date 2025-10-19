# poetry run

> Run a command inside Poetry's virtual environment.
> More information: <https://python-poetry.org/docs/cli/#run>.

- Run a shell inside the project's virtual environment:

`poetry run {{bash}}`

- Execute a Python script with arguments:

`poetry run python {{path/to/script.py}} {{script_arguments}}`

- Run test suite with pytest:

`poetry run pytest {{path/to/tests}}`

- Run a command with arguments:

`poetry run {{command}} {{arguments}}`
