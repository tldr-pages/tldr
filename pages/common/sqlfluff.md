# sqlfluff

> Lint and auto-format SQL files across multiple dialects.
> More information: <https://docs.sqlfluff.com/en/stable/reference/cli.html>.

- Lint a SQL file with a specific dialect:

`sqlfluff lint --dialect {{dialect}} {{path/to/file.sql}}`

- Lint all SQL files in a directory with a specific dialect:

`sqlfluff lint --dialect {{dialect}} {{path/to/directory}}`

- Auto-format a SQL file with a specific dialect:

`sqlfluff format --dialect {{dialect}} {{path/to/file.sql}}`

- Automatically fix linting violations in a SQL file:

`sqlfluff fix --dialect {{dialect}} --rules {{rule1,rule2}} {{path/to/file.sql}}`

- Show all supported SQL dialects:

`sqlfluff dialects`
