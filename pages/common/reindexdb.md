# reindexdb

> Rebuild indexes in a PostgreSQL database.
> More information: <https://www.postgresql.org/docs/current/app-reindexdb.html>.

- Reindex a specific database:

`reindexdb {{database_name}}`

- Reindex a specific database using connection options:

`reindexdb {{[-h|--host]}} {{hostname}} {{[-p|--port]}} {{port}} {{[-U|--username]}} {{username}} {{database_name}}`

- Reindex all databases:

`reindexdb {{[-a|--all]}}`

- Reindex a specific table in a database:

`reindexdb {{[-t|--table]}} {{table_name}} {{database_name}}`

- Reindex a specific index in a database:

`reindexdb {{[-i|--index]}} {{index_name}} {{database_name}}`

- Reindex a specific schema in a database:

`reindexdb {{[-S|--schema]}} {{schema_name}} {{database_name}}`

- Reindex with verbose output:

`reindexdb {{[-v|--verbose]}} {{database_name}}`

- Reindex a database using multiple parallel jobs:

`reindexdb {{[-j|--jobs]}} {{number_of_jobs}} {{database_name}}`
