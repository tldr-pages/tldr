# usql

> Interfaz de línea de comandos universal para bases de datos SQL.
> Más información: <https://github.com/xo/usql>.

- Conecta a una base de datos específica:

`usql {{sqlserver|mysql|postgres|sqlite3|...}}://{{nombre_usuario}}:{{contraseña}}@{{host}}:{{puerto}}/{{nombre_base_de_datos}}`

- Ejecuta comandos desde un archivo:

`usql --file={{ruta/al/query.sql}}`

- Ejecuta un comando SQL específico:

`usql --command="{{comando_sql}}"`

- Ejecuta un comando SQL en el intérprete de comandos de `usql`:

`{{prompt}}=> {{comando}}`

- Muestra el esquema de la base de datos:

`{{prompt}}=> \d`

- Exporta los resultados de la consulta a un archivo específico:

`{{prompt}}=> \g {{ruta/a/archivo_con_resultados}}`

- Importa datos de un archivo CSV a una tabla específica:

`{{prompt}}=> \copy {{ruta/a/datos.csv}} {{nombre_de_tabla}}`
