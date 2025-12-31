# duckdb

> Client for DuckDB, an in-process analytical SQL engine.
> More information: <https://duckdb.org/docs/stable/clients/cli/arguments>.

- Start an interactive shell with a transient in-memory database:

`duckdb`

- Start an interactive shell on a database file. If the file does not exist, a new database is created:

`duckdb {{path/to/dbfile}}`

- Query a CSV, JSON, or Parquet file using SQL:

`duckdb -c "{{SELECT * FROM 'data_source.[csv|csv.gz|json|json.gz|parquet]'}}"`

- Directly query a CSV, JSON, or Parquet file using the `file` view:

`duckdb {{data_source.[csv|csv.gz|json|json.gz|parquet]}} -c "{{ SELECT * FROM file }}"`

- Run an SQL script:

`duckdb -f {{path/to/script.sql}}`

- Run query on database file and keep the interactive shell open:

`duckdb {{path/to/dbfile}} -cmd "{{SELECT DISTINCT * FROM tbl}}"`

- Read CSV from `stdin` and write CSV to `stdout`:

`cat {{path/to/source.csv}} | duckdb -c "{{COPY (FROM read_csv('/dev/stdin')) TO '/dev/stdout' WITH (FORMAT CSV, HEADER)}}"`

- Start the DuckDB UI, a web interface with notebooks:

`duckdb -ui`
