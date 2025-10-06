# reindexdb

> Rebuild indexes in a PostgreSQL database.
> More information: <https://www.postgresql.org/docs/current/app-reindexdb.html>.

- Reindex a specific database:

`reindexdb {{database_name}}`

- Reindex a specific database using connection options:

`reindexdb {{database_name}} {{[-h|--host]}} {{hostname}} {{[-p|--port]}} {{port}} {{[-U|--username]}} {{username}}`

- Reindex all databases:

`reindexdb {{[-a|--all]}}`

- Reindex a specific table in a database:

`reindexdb {{database_name}} {{[-t|--table]}} {{table_name}}`

- Reindex a specific index in a database:

`reindexdb {{database_name}} {{[-i|--index]}} {{index_name}}`

- Reindex a specific schema in a database:

`reindexdb {{database_name}} {{[-S|--schema]}} {{schema_name}}`

- Reindex with verbose output:

`reindexdb {{database_name}} {{[-v|--verbose]}}`

- Reindex a database using multiple parallel jobs:

`reindexdb {{database_name}} {{[-j|--jobs]}} {{number_of_jobs}}`
