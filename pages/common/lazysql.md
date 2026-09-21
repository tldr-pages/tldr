# lazysql

> Cross-platform TUI database management tool.
> Supports MySQL, PostgreSQL, SQLite, and MSSQL.
> More information: <https://github.com/jorgerojas26/lazysql>.

- Start in picker mode to choose from the saved connections:

`lazysql`

- Connect to a database using a connection URL:

`lazysql "{{postgres://user:password@localhost:5432/database}}"`

- Open a SQLite database file:

`lazysql {{path/to/database.sqlite3}}`

- Connect in read-only mode:

`lazysql --read-only "{{connection_url}}"`

- Use a specific configuration file:

`lazysql --config {{path/to/config.toml}}`

- Write logs to a specific file at a specific level:

`lazysql --logfile {{path/to/lazysql.log}} --loglevel {{debug}}`

- Display version:

`lazysql --version`
