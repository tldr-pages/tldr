# mysqldump

> Crea una copia de seguridad (backup) de bases de datos MySQL.
> Vea también `mysql` para restaurar bases de datos.
> Más información: <https://dev.mysql.com/doc/refman/en/mysqldump.html>.

- Crea un backup (se le pedirá la contraseña al usuario):

`mysqldump --user {{usuario}} --password {{nombre_base_de_datos}} --result-file={{ruta/al/archivo.sql}}`

- Crea un backup de una tabla específica redireccionando la salida a un archivo (se le pedirá la contraseña al usuario):

`mysqldump --user {{usuario}} --password {{nombre_base_de_datos}} {{nombre_de_tabla}} > {{ruta/al/archivo.sql}}`

- Crea un backup de todas las bases de datos y redirige la salida a un archivo (se le pedirá la contraseña al usuario):

`mysqldump --user {{usuario}} --password --all-databases > {{ruta/al/archivo.sql}}`

- Crea un backup de todas las bases de datos de un host remoto redirigiendo la salida a un archivo (se le pedirá la contraseña al usuario):

`mysqldump --host={{ip_o_nombre_de_host}} --user {{usuario}} --password --all-databases > {{ruta/al/archivo.sql}}`
