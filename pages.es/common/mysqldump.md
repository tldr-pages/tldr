# mysqldump

> Crea una copia de seguridad de bases de datos MySQL.
> Vea también `mysql` para restaurar bases de datos.
> Más información: <https://dev.mysql.com/doc/refman/en/mysqldump.html>.

- Crea un backup (se le pedirá la contraseña al usuario):

`mysqldump --user {{usuario}} --password {{nombre_base_de_datos}} -r {{ruta/al/archivo.sql}}`

- Crea un backup de todas las bases de datos y redirige la salida a un archivo (se le pedirá la contraseña al usuario):

`mysqldump --user {{usuario}} --password --all-databases > {{ruta/al/archivo.sql}}`

- Crea un backup de una única tabla de una base de datos (se le pedirá la contraseña al usuario):

`mysqldump --user {{usuario}} --password {{nombre_base_de_datos}} {{nombre_tabla}} -r {{ruta/al/archivo.sql}}`
