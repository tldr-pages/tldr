# usql

> Universal CLI interface for SQL databases.
> More information: <https://github.com/xo/usql>.

- Connect to a specific database with SSL disabled:

`usql {{sqlserver|mysql|postgres|sqlite3|...}}://{{username}}:{{password}}@{{host}}:{{port}}/{{database_name}}?sslmode=disable`

- Execute commands from a file:

`usql --file={{path/to/query.sql}}`

- Execute a specific SQL command:

`usql --command="{{sql_command}}"`

- List databases available on the server:

`usql --list-databases`
