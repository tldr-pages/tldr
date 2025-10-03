# vacuumdb

> Garbage-collect and analyze a PostgreSQL database.
> More information: <https://www.postgresql.org/docs/current/app-vacuumdb.html>.

- Vacuum a specific database:

`vacuumdb {{database_name}}`

- Vacuum all databases:

`vacuumdb --all`

- Vacuum a specific table in a database:

`vacuumdb --table={{table_name}} {{database_name}}`

- Vacuum and update statistics for the query planner:

`vacuumdb --analyze {{database_name}}`

- Perform a full vacuum (more aggressive, locks tables, rewrites the whole table):

`vacuumdb --full {{database_name}}`

- Vacuum with verbose output:

`vacuumdb --verbose {{database_name}}`

- Vacuum a database using multiple parallel jobs:

`vacuumdb --jobs={{number_of_jobs}} {{database_name}}`
