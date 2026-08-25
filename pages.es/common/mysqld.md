# mysqld

> Inicia el servidor de bases de datos MySQL.
> Más información: <https://dev.mysql.com/doc/refman/en/mysqld.html>.

- Inicia el servidor de bases de datos MySQL:

`mysqld`

- Inicia el servidor, mostrando los mensajes de error en la consola:

`mysqld --console`

- Inicia el servidor, guardando la salida de registro en un archivo de registro personalizado:

`mysqld --log={{ruta/al/archivo.log}}`

- Muestra los argumentos predeterminados y sus valores y salir:

`mysqld --print-defaults`

- Inicia el servidor, leyendo los argumentos y valores de un archivo:

`mysqld --defaults-file={{ruta/al/archivo}}`

- Inicia el servidor y escucha en un puerto personalizado:

`mysqld --port={{puerto}}`

- Muestra la ayuda:

`mysqld --verbose --help`
