# ruff

> Lint and format Python code.
> See also: `black`.
> More information: <https://docs.astral.sh/ruff/>.

- Check for linting errors in a file or directory:

`ruff check {{path/to/file_or_directory}}`

- Check and automatically fix linting errors:

`ruff check --fix {{path/to/file_or_directory}}`

- Format a file or directory:

`ruff format {{path/to/file_or_directory}}`

- Check formatting without applying changes:

`ruff format --check {{path/to/file_or_directory}}`

- List all available lint rules:

`ruff rule --all`

- Display help for linting:

`tldr ruff check`

- Display help for formatting:

`tldr ruff format`
