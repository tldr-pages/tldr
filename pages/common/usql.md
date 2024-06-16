# usql

> Universal CLI interface for SQL databases.
> More information: <https://github.com/xo/usql>.

- Connect to a specific database:

`usql {{sqlserver|mysql|postgres|sqlite3|...}}://{{username}}:{{password}}@{{host}}:{{port}}/{{database_name}}`

- Execute commands from a file:

`usql --file={{path/to/query.sql}}`

- Execute a specific SQL command:

`usql --command="{{sql_command}}"`

- Run an SQL command in the `usql` prompt:

`{{prompt}}=> {{command}}`

- Display the database schema:

`{{prompt}}=> \d`

- Export query results to a specific file:

`{{prompt}}=> \g {{/path/to/results.txt}}`

- Import data from a CSV file into a specific table:

`{{prompt}}=> \copy {{/path/to/data.csv}} {{table_name}}`
