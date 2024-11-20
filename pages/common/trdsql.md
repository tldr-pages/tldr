# trdsql

> Execute SQL on CSV, LTSV, JSON, YAML, and TBLN files.
> More information: <https://noborus.github.io/trdsql/>.

- Convert object data from multiple JSON files to a CSV file with header (`-oh`) & double quote:

`trdsql -ocsv -oh "SELECT * FROM {{path/to/file/*.json}}" | sed 's/\([^,]*\)/"&"/g'  > {{path/to/file.csv}}`

- Interpret JSON list as a table & put object inside as columns (path/to/file.json: `{"list":[{"age":"26","name":"Tanaka"}]}`):

`trdsql "SELECT * FROM {{path/to/file.json}}::.list`

- Complex SQL data manipulation with multiple CSV files with first line is header (`-ih`):

`trdsql -icsv -ih "SELECT id,name,phone_number FROM {{path/to/file*.csv}} WHERE phone_number != '' ORDER BY id GROUP BY field1"`

- Merge content of 2 CSV files to one CSV file:

`trdsql "SELECT column1, colum2 FROM {{path/to/file1.csv}} UNION SELECT column1,column2 FROM {{path/to/file2.csv}}"`

- Simple connection to PostgreSQL database:

`trdsql -driver postgres -dsn "host=localhost port=5433 dbname=trdsql_test" "SELECT 1"`

- Create table data to MySQL database from CSV file:

`trdsql -driver mysql -dsn "noborus:noborus@/trdsql_test" -ih "CREATE TABLE fruits (num int, name varchar(20)) AS SELECT id AS num,name FROM {{path/to/header_file.csv}}"`

- Simple showing data from compress log files:

`trdsql -iltsv "SELECT * FROM {{path/to/access.log.gz}}"`
