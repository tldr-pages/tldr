# pg_dump

> Extrae una base de datos PostgreSQL en un archivo de script u otro archivo de almacenamiento.
> Más información: <https://www.postgresql.org/docs/current/app-pgdump.html>.

- Vuelca la base de datos en un archivo script-SQL:

`pg_dump {{nombre_base_de_datos}} > {{archivo_resultado.sql}}`

- Igual que antes usando además un nombre de usuario:

`pg_dump {{[-U|--username]}} {{usuario}} {{nombre_base_de_datos}} > {{archivo_resultado.sql}}`

- Lo mismo que antes usando además equipo y puerto:

`pg_dump {{[-h|--host]}} {{equipo}} {{[-p|--port]}} {{puerto}} {{nombre_base_de_datos}} > {{archivo_resultado.sql}}`

- Vuelca una base de datos en un archivo de formato personalizado:

`pg_dump {{[-F|--format]}} {{[c|custom]}} {{nombre_base_de_datos}} > {{archivo_resultado.dump}}`

- Recupera solo datos de bases de datos en un archivo script-SQL:

`pg_dump {{[-a|--data-only]}} {{nombre_base_de_datos}} > {{ruta/al/archivo_resultado.sql}}`

- Vuelca solo el esquema (definiciones de datos) en un archivo script-SQL:

`pg_dump {{[-s|--schema-only]}} {{nombre_base_de_datos}} > {{ruta/al/archivo_resultado.sql}}`
