# cypher-shell

> Abre una sesión interactiva y ejecuta consultas Cypher contra una instancia Neo4j.
> Vea también: `neo4j-admin`, `mysql`.
> Más información: <https://neo4j.com/docs/operations-manual/current/cypher-shell/>.

- Se conecta a una instancia local en el puerto por defecto (`neo4j://localhost:7687`):

`cypher-shell`

- Se conecta a una instancia remota:

`cypher-shell --address neo4j://{{host}}:{{puerto}}`

- Se conecta y proporciona credenciales de seguridad:

`cypher-shell --username {{usuario}} --password {{contraseña}}`

- Se conecta a una base de datos específica:

`cypher-shell --database {{nombre_base_de_datos}}`

- Ejecuta sentencias Cypher en un archivo y lo cierra:

`cypher-shell --file {{ruta/al/archivo.cypher}}`

- Activa el registro en un archivo:

`cypher-shell --log {{ruta/al/archivo.log}}`

- Muestra la ayuda:

`cypher-shell --help`
