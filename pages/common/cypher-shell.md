# cypher-shell

> Open an interactive session and run Cypher queries against a Neo4j instance.
> See also: `neo4j-admin`, `mysql`.
> More information: <https://neo4j.com/docs/operations-manual/current/tools/cypher-shell/>.

- Connect to a local instance on the default port (`neo4j://localhost:7687`):

`cypher-shell`

- Connect to a remote instance:

`cypher-shell --address neo4j://{{host}}:{{port}}`

- Connect and supply security credentials:

`cypher-shell --username {{username}} --password {{password}}`

- Connect to a specific database:

`cypher-shell --database {{database_name}}`

- Execute Cypher statements in a file and close:

`cypher-shell --file {{path/to/file.cypher}}`

- Enable logging to a file:

`cypher-shell --log {{path/to/file.log}}`

- Display help:

`cypher-shell --help`
