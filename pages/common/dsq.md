# dsq

> Run SQL queries against JSON, CSV, Excel, Parquet, and other file formats.
> More information: <https://github.com/multiprocessio/dsq>.

- Query a CSV file:

`dsq {{path/to/file.csv}} "SELECT * FROM {} WHERE {{column}} = '{{value}}'"` 

- Query a JSON file and output as CSV:

`dsq --pretty {{path/to/file.json}} "SELECT {{column1}}, {{column2}} FROM {}"`

- Join two files:

`dsq {{path/to/file1.csv}} {{path/to/file2.json}} "SELECT * FROM {0} JOIN {1} ON {0}.{{id}} = {1}.{{id}}"`

- Read from stdin:

`cat {{path/to/file.csv}} | dsq --stdin csv "SELECT COUNT(*) FROM {}"`

- Output results as JSON:

`dsq {{path/to/file.csv}} "SELECT * FROM {}" | jq`
