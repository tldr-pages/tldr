# pg_dumpall

> Extrae un grupo de bases de datos PostgreSQL en un archivo de script u otro archivo de almacenamiento.
> Más información: <https://www.postgresql.org/docs/current/app-pg-dumpall.html>.

- Vuelca todas las bases de datos:

`pg_dumpall > {{ruta/al/archivo.sql}}`

- Vuelca todas las bases de datos utilizando un nombre de usuario específico:

`pg_dumpall {{[-U|--username]}} {{usuario}} > {{ruta/al/archivo.sql}}`

- Lo mismo que antes, usando un equipo y puerto:

`pg_dumpall {{[-h|--host]}} {{equipo}} {{[-p|--port]}} {{puerto}} > {{archivo_resultado.sql}}`

- Recupera solo datos de las bases de datos en un archivo script-SQL:

`pg_dumpall {{[-a|--data-only]}} > {{ruta/al/archivo.sql}}`

- Vuelca solo el esquema (definiciones de datos) en un archivo script-SQL:

`pg_dumpall {{[-s|--schema-only]}} > {{archivo_resultado.sql}}`
