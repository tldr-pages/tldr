# duckdb

> Command-line client for DuckDB, an in-process analytical SQL engine.
> More information: <https://duckdb.org>.

- Start an interactive shell with a transient in-memory database:

`duckdb`

- Start an interactive shell on a database file. If the file does not exist, a new database is created:

`duckdb {{path/to/dbfile.[db|duckdb]}}`

- Load CSV or Parquet file to a table and quit:

`duckdb {{path/to/dbfile.[db|duckdb]}} -c "{{CREATE OR REPLACE TABLE tbl AS FROM 'data_source.[csv|parquet]'}}"`

- Run query on database file and keep interactive shell open:

`duckdb {{path/to/dbfile.[db|duckdb]}} -cmd "{{SELECT DISTINCT * FROM tbl}}"`

- Run SQL queries in file on database and keep interactive shell open:

`duckdb {{path/to/dbfile.[db|duckdb]}} -init {{path/to/script.sql}}`

- Open database in read-only mode:

`duckdb -readonly {{path/to/dbfile.[db|duckdb]}}`

- Display help:

`duckdb -help`
