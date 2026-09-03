# vacuumdb

> Garbage-collect and analyze a PostgreSQL database.
> More information: <https://www.postgresql.org/docs/current/app-vacuumdb.html>.

- Vacuum a specific database:

`vacuumdb {{database_name}}`

- Vacuum all databases:

`vacuumdb {{[-a|--all]}}`

- Vacuum a specific table in a database:

`vacuumdb {{database_name}} {{[-t|--table]}} {{table_name}}`

- Vacuum and update statistics for the query planner:

`vacuumdb {{database_name}} {{[-z|--analyze]}}`

- Perform a full vacuum (more aggressive, locks tables, rewrites the whole table):

`vacuumdb {{database_name}} {{[-f|--full]}}`

- Vacuum with verbose output:

`vacuumdb {{database_name}} {{[-v|--verbose]}}`

- Vacuum a database using multiple parallel jobs:

`vacuumdb {{database_name}} {{[-j|--jobs]}} {{number_of_jobs}}`
