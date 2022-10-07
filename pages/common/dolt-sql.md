# dolt sql

> Run a SQL query. Multiple SQL statements must be separated by semicolons.
> More information: <https://docs.dolthub.com/cli-reference/cli#dolt-sql>.

- Run a single query:

`dolt sql -q "INSERT INTO t values (1, 3);"`

- Run multiple SQL statements:

`dolt sql <<SQL ALTER TABLE t ADD c INT; INSERT INTO t VALUES (1, 2, 1); SQL`

- List all saved queries:

`dolt sql --list-saved`
