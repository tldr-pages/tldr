# neo4j-admin

> Gestiona y administra un Neo4j DBMS (Sistema de Gestión de Bases de Datos).
> Más información: <https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/>.

- Inicia el DBMS:

`neo4j-admin server start`

- Detiene el DBMS:

`neo4j-admin server stop`

- Establece la contraseña inicial del usuario por defecto `neo4j` (requisito para el primer arranque del DBMS):

`neo4j-admin dbms set-initial-password {{nombre_base_de_datos}}`

- Crea un archivo (dump) de una base de datos sin conexión a un fichero llamado `nombre_base_de_datos.dump`:

`neo4j-admin database dump --to-path={{ruta/aL/directorio}} {{nombre_base_de_datos}}`

- Carga una base de datos desde un archivo llamado `nombre_base_de_datos.dump`:

`neo4j-admin database load --from-path={ruta/aL/directorio}} {{nombre_base_de_datos}} --overwrite-destination=true`

- Carga una base de datos desde un archivo especificado a través de `stdin`:

`neo4j-admin database load --from-stdin {{nombre_base_de_datos}} --overwrite-destination=true < {{ruta/a/nombre_archivo.dump}}`

- Muestra ayuda:

`neo4j-admin --help`
