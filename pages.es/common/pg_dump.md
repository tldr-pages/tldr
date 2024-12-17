# pg_dump

> Extrae una base de datos PostgreSQL en un archivo de script u otro archivo de almacenamiento.
> Más información: <https://www.postgresql.org/docs/current/app-pgdump.html>.

- Vuelca la base de datos en un archivo guión-SQL:

`pg_dump {{nombre_base_de_datos}} > {{archivo_resultado.sql}}`

- Igual que antes usando además un nombre de usuario:

`pg_dump -U {{usuario}} {{nombre_base_de_datos}} > {{archivo_resultado.sql}}`

- Lo mismo que antes usando además equipo y puerto:

`pg_dump -h {{equipo}} -p {{puerto}} {{nombre_base_de_datos}} > {{archivo_resultado.sql}}`

- Vuelca una base de datos en un archivo de formato personalizado:

`pg_dump -Fc {{nombre_base_de_datos}} > {{archivo_resultado.dump}}`

- Recupera solo datos de bases de datos en un archivo script-SQL:

`pg_dump -a {{nombre_base_de_datos}} > {{ruta/al/archivo_resultado.sql}}`

- Vuelca solo el esquema (definiciones de datos) en un archivo script-SQL:

`pg_dump -s {{nombre_base_de_datos}} > {{ruta/al/archivo_resultado.sql}}`
