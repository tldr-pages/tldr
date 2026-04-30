# sqlfluff

> Lint and auto-format SQL files across multiple dialects.
> More information: <https://docs.sqlfluff.com/en/stable/reference/cli.html>.

- Lint a SQL file or directory with a specific dialect:

`sqlfluff lint {{[-d|--dialect]}} {{dialect}} {{path/to/file_or_directory}}`

- Auto-format a SQL file or directory with a specific dialect:

`sqlfluff format --dialect {{dialect}} {{path/to/file_or_directory}}`

- Automatically fix linting violations in a SQL file or directory:

`sqlfluff fix --dialect {{dialect}} --rules {{rule1,rule2}} {{path/to/file_or_directory}}`

- Parse a SQL file or directory and display the parse tree:

`sqlfluff parse --dialect {{dialect}} {{path/to/file_or_directory}}`

- Show all supported SQL dialects:

`sqlfluff dialects`
