# sqlite3

> The command-line interface to SQLite 3, which is a self-contained file-based embedded SQL engine.
> More information: <https://sqlite.org>.

- Start an interactive shell with a new database:

`sqlite3`

- Open an interactive shell against an existing database:

`sqlite3 {{path/to/database.sqlite3}}`

- Execute an SQL statement against a database and then exit:

`sqlite3 {{path/to/database.sqlite3}} '{{SELECT * FROM some_table;}}'`
