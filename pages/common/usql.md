# usql

> Universal CLI interface for SQL databases.
> More information: <https://github.com/xo/usql#using>.

- Connect to a specific database:

`usql {{sqlserver|mysql|postgres|sqlite3|...}}://{{username}}:{{password}}@{{host}}:{{port}}/{{database_name}}`

- Execute commands from a file:

`usql --file={{path/to/query.sql}}`

- Execute a specific SQL command:

`usql --command="{{sql_command}}"`

- [Interactive] Run an SQL command in the `usql` prompt:

`{{command}}`

- [Interactive] Display the database schema:

`\d`

- [Interactive] Export query results to a specific file:

`\g {{path/to/file_with_results}}`

- [Interactive] Import data from a CSV file into a specific table:

`\copy {{path/to/data.csv}} {{table_name}}`
