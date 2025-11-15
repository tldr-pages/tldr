# trdsql

> Ejecuta SQL en archivos CSV, LTSV, JSON, YAML y TBLN.
> Más información: <https://noborus.github.io/trdsql/>.

- Convierte datos de objetos de varios archivos JSON a un archivo CSV con encabezado (`-oh`) y comillas dobles:

`trdsql -ocsv -oh "SELECT * FROM {{ruta/al/archivo/*.json}}" | sed 's/\([^,]*\)/«&»/g' > {{ruta/al/archivo.csv}}`

- Interpreta una lista JSON como tabla y pone objetos dentro como columnas ( ruta/al/archivo.json: `{"lista":[{"edad":"26", "nombre":"Tanaka"}]}`):

`trdsql "SELECT * FROM {{ruta/al/archivo.json}}::.list`

- Manipula una consulta SQL compleja con datos de varios archivos CSV cuya primera línea es la cabecera (`-ih`):

`trdsql -icsv -ih "SELECT {{columna1,columna2}} FROM {{ruta/al/archivo*.csv}} WHERE column2 != '' ORDER BY columna1 GROUP BY columna1"`

- Combina el contenido de 2 archivos CSV en un archivo CSV:

`trdsql "SELECT {{columna1,columna2}} FROM {{ruta/al/archivo1.csv}} UNION SELECT {{columna1,columna2}} FROM {{ruta/al/archivo2.csv}}"`

- Se conecta a la base de datos PostgreSQL:

`trdsql -driver postgres -dsn "host={{nombre_del_host}} port={{5433}} dbname={{nombre_de_la_base_de_datos}}" "SELECT 1"`

- Crea una tabla de datos en una base de datos MySQL a partir de un archivo CSV:

`trdsql -driver mysql -dsn "{{usuario}}:{{contraseña}}@{{nombre_del_host}}/{{base_de_datos}}" -ih "CREATE TABLE {{tabla}} ({{columna1}} int, {{columna2}} varchar(20)) AS SELECT {{columna3}} AS {{columna1}},{{columna2}} FROM {{ruta/a/archivo_cabecera.csv}}"`

- Muestra datos de archivos de registro comprimidos:

`trdsql -iltsv "SELECT * FROM {{ruta/a/acceso.log.gz}}"`
