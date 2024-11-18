# trdsql

> CLI tool that executes SQL on CSV, LTSV, JSON, YAML, TBLN files.
> More information: <https://noborus.github.io/trdsql/>.

- Convert array data from a JSON file to a CSV file (with double quote):

`trdsql -ocsv "SELECT * FROM example.json" | sed 's/\([^,]*\)/"&"/g'  > example.csv`

- Convert object data from multiple JSON files to a CSV file (with double quote):

`trdsql -ocsv "SELECT * FROM example/*.json" | sed 's/\([^,]*\)/"&"/g'  > example.csv`

- Interpret JSON list as a table & put object inside as columns (example.json: `{"list":[{"age":"26","name":"Tanaka"}]}`):

`trdsql "SELECT * FROM example.json::.list`

- Complex SQL data manipulation with multiple CSV files:

`trdsql -icsv "SELECT id,name,phone_number FROM example*.csv WHERE phone_number != '' ORDER BY id GROUP BY field1"`

- Cross join 2 csv files:

`trdsql "SELECT * FROM a.csv CROSS JOIN b.csv"`

- Simple connection to PostgreSQL database:

`trdsql -driver postgres -dsn "host=localhost port=5433 dbname=trdsql_test" "SELECT 1"`

- Create table data to MySQL database from CSV file:

`trdsql -driver mysql -dsn "noborus:noborus@/trdsql_test" -ih "CREATE TABLE fruits (num int, name varchar(20)) AS SELECT id AS num,name FROM header.csv"`

- Simple showing data from compress log files:

`trdsql -iltsv "SELECT * FROM access.log.2.gz"`
