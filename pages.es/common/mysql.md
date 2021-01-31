# mysql

> Herramienta de línea de comandos para gestionar bases de datos MySQL
> Más información: <https://www.mysql.com/>.

- Conecta a una base de datos:

`mysql {{nombre_base_de_datos}}`

- Conecta a una base de datos con el usuario `usuario` y se le pedirá la contraseña:

`mysql -u {{usuario}} --password {{nombre_base_de_datos}}`

- Conecta a una base de datos en otra máquina:

`mysql -h {{maquina_remota}} {{nombre_base_de_datos}}`

- Conecta a una base de datos a través de un socket unix:

`mysql --socket {{ruta/al/socket.sock}}`

- Ejecuta comandos SQL contenidos en un script:

`mysql -e "source {{archivo.sql}}" {{nombre_base_de_datos}}`

- Restaura una base de datos a partir de una copia de seguridad creada con `mysqldump` (y se le pedirá la contraseña al usuario):

`mysql --user {{usuario}} --password {{nombre_base_de_datos}} < {{ruta/al/backup.sql}}`

- Restaura todas las bases de datos en una copia de seguridad (y se le pedirá la contraseña al usuario):

`mysql --user {{usuario}} --password < {{ruta/al/backup.sql}}`
