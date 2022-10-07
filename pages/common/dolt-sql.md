# dolt sql

> Runs a SQL query you specify. Multiple SQL statements must be separated by semicolons.
> More information: <https://docs.dolthub.com/cli-reference/cli#dolt-sql>.

- Runs a single query

`dolt sql -q "INSERT INTO t values (1, 3);"`

- Runs multiple SQL statements:

`dolt sql <<SQL
ALTER TABLE t ADD c INT;
INSERT INTO t VALUES (1, 2, 1);
SQL`

- List all saved queries.

`dolt sql --list-saved`
