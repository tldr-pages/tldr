# duckdb

> Command-line client for DuckDB, an in-process analytical SQL engine.
> More information: <https://duckdb.org>.

- Start an interactive shell with a transient in-memory database:

`duckdb`

- Start an interactive shell on a database file. If the file does not exist, a new database is created:

`duckdb {{path/to/dbfile}}`

- Directly query a CSV, JSON, or Parquet file:

`duckdb -c "{{SELECT * FROM 'data_source.[csv|csv.gz|json|json.gz|parquet]'}}"`

- Run a SQL script:

`duckdb -c ".read {{path/to/script.sql}}"`

- Run query on database file and keep the interactive shell open:

`duckdb {{path/to/dbfile}} -cmd "{{SELECT DISTINCT * FROM tbl}}"`

- Run SQL queries in file on database and keep the interactive shell open:

`duckdb {{path/to/dbfile}} -init {{path/to/script.sql}}`

- Read CSV from `stdin` and write CSV to `stdout`:

`cat {{path/to/source.csv}} | duckdb -c "{{COPY (FROM read_csv_auto('/dev/stdin')) TO '/dev/stdout' WITH (FORMAT CSV, HEADER)}}"`

- Display help:

`duckdb -help`
