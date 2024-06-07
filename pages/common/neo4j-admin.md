# neo4j-admin

> Manage and administer a Neo4j DBMS.
> More information: <https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/>.

- Start the Neo4j DBMS:

`neo4j-admin server start`

- Stop the Neo4j DBMS:

`neo4j-admin server stop`

- Set the initial password of the default `neo4j` user (required before the first DBMS start):

`neo4j-admin dbms set-initial-password {{database_name}}`

- Create an archive (dump) of an offline database to a file named `database_name.dump`:

`neo4j-admin database dump --to-path={{path/to/dumps}} {{database_name}}`

- Load a database from an archive named `database_name.dump`:

`neo4j-admin database load --from-path={{path/to/dumps}} {{database_name}} --overwrite-destination=true`

- Load a database from a specified archive file through `stdin`:

`cat {{path/to/filename.dump}} | neo4j-admin database load --from-stdin {{database_name}} --overwrite-destination=true`

- Get help:

`neo4j-admin --help`
