# trdsql

> Execute SQL on CSV, LTSV, JSON, YAML, and TBLN files.
> More information: <https://noborus.github.io/trdsql/>.

- Convert object data from multiple JSON files to a CSV file with header (`-oh`) and double quote:

`trdsql -ocsv -oh "SELECT * FROM {{path/to/file/*.json}}" | sed 's/\([^,]*\)/"&"/g' > {{path/to/file.csv}}`

- Interpret JSON list as a table and put objects inside as columns (path/to/file.json: `{"list":[{"age":"26","name":"Tanaka"}]}`):

`trdsql "SELECT * FROM {{path/to/file.json}}::.list`

- Manipulate complex SQL query with data from multiple CSV files with first line is header (`-ih`):

`trdsql -icsv -ih "SELECT {{column1,column2}} FROM {{path/to/file*.csv}} WHERE column2 != '' ORDER BY column1 GROUP BY column1"`

- Merge content of 2 CSV files to one CSV file:

`trdsql "SELECT {{column1,colum2}} FROM {{path/to/file1.csv}} UNION SELECT {{column1,column2}} FROM {{path/to/file2.csv}}"`

- Connect to PostgreSQL database:

`trdsql -driver postgres -dsn "host={{hostname}} port={{5433}} dbname={{database_name}}" "SELECT 1"`

- Create table data to MySQL database from CSV file:

`trdsql -driver mysql -dsn "{{username}}:{{password}}@{{hostname}}/{{database}}" -ih "CREATE TABLE {{table}} ({{column1}} int, {{colum2}} varchar(20)) AS SELECT {{column3}} AS {{column1}},{{column2}} FROM {{path/to/header_file.csv}}"`

- Show data from compress log files:

`trdsql -iltsv "SELECT * FROM {{path/to/access.log.gz}}"`
