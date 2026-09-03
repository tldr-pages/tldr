# clusterdb

> Cluster (reorganize) a PostgreSQL database.
> More information: <https://www.postgresql.org/docs/current/app-clusterdb.html>.

- Cluster a specific database:

`clusterdb {{database_name}}`

- Cluster all databases:

`clusterdb {{[-a|--all]}}`

- Cluster a specific table in a database:

`clusterdb {{database_name}} {{[-t|--table]}} {{table_name}}`
