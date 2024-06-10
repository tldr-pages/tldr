# neo4j-admin

> Manage and administer a Neo4j DBMS (Database Management System).
> More information: <https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/>.

- Start the DBMS:

`neo4j-admin server start`

- Stop the DBMS:

`neo4j-admin server stop`

- Set the initial password of the default `neo4j` user (prerequisite for the first start of the DBMS):

`neo4j-admin dbms set-initial-password {{database_name}}`

- Create an archive (dump) of an offline database to a file named `database_name.dump`:

`neo4j-admin database dump --to-path={{path/to/directory}} {{database_name}}`

- Load a database from an archive named `database_name.dump`:

`neo4j-admin database load --from-path={{path/to/directory}} {{database_name}} --overwrite-destination=true`

- Load a database from a specified archive file through `stdin`:

`neo4j-admin database load --from-stdin {{database_name}} --overwrite-destination=true < {{path/to/filename.dump}}`

- Display help:

`neo4j-admin --help`
