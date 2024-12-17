# pg_restore

> Restaura una base de datos PostgreSQL de un archivo creado con pg_dump.
> Más información: <https://www.postgresql.org/docs/current/app-pgrestore.html>.

- Restaura un archivo en una base de datos existente:

`pg_restore -d {{nombre_base_de_datos}} {{archivo_de_datos.dump}}`

- Igual que antes, utilizando un nombre de usuario:

`pg_restore -U {{usuario}} -d {{nombre_base_de_datos}} {{archivo_de_datos.dump}}`

- Lo mismo que antes, usando un nombre de equipo y puerto:

`pg_restore -h {{equipo}} -p {{puerto}} -d {{nombre_base_de_datos}} {{archivo_de_datos.dump}}`

- Lista los objetos de bases de datos incluidos en el archivo:

`pg_restore --list {{archivo_de_datos.dump}}`

- Limpia los objetos de base de datos antes de crearlos:

`pg_restore --clean -d {{nombre_base_de_datos}} {{archivo_de_datos.dump}}`

- Utiliza múltiples trabajos para hacer la restauración:

`pg_restore -j {{2}} -d {{nombre_base_de_datos}} {{archivo_de_datos.dump}}`
