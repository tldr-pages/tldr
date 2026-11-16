# usql

> Interfaz de línea de comandos universal para bases de datos SQL.
> Más información: <https://github.com/xo/usql#using>.

- Conecta a una base de datos específica:

`usql {{sqlserver|mysql|postgres|sqlite3|...}}://{{usuario}}:{{contraseña}}@{{host}}:{{puerto}}/{{nombre_base_de_datos}}`

- Ejecuta comandos desde un archivo:

`usql {{[-f|--file]}} {{ruta/al/query.sql}}`

- Ejecuta un comando SQL específico:

`usql {{[-c|--command]}} "{{comando_sql}}"`

- [Interactivo] Ejecuta un comando SQL en el intérprete de comandos de `usql`:

`{{comando}}`

- [Interactivo] Muestra el esquema de la base de datos:

`\d`

- [Interactivo] Exporta los resultados de la consulta a un archivo específico:

`\g {{ruta/al/archivo_con_resultados}}`

- [Interactivo] Importa datos de un archivo CSV a una tabla específica:

`\copy {{ruta/a/datos.csv}} {{nombre_de_tabla}}`
