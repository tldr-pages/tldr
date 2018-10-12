# mlr

> Miller is like awk, sed, cut, join, and sort for name-indexed data such as CSV, TSV, and tabular JSON.

- Pretty-print a CSV file in a tabular format:

`mlr --icsv --opprint cat {{example.csv}}`

- Sort first alphabetically on field1, and then sort in descending numerical order on field2:

`mlr --icsv --opprint sort -f {{field1}} -nr {{field2}} {{example.csv}}`

- Convert CSV to JSON, performing calculations and outputting those calculations:

`mlr --icsv --ojson put '${{newField1}} = ${{oldFieldA}}/${{oldFieldB}}; ${{newField2}} = toupper(${{oldFieldC}})' {{example.csv}}`

- Retrieve records from a MySQL database and format the output as vertical JSON:

`mysql --database={{exampledatabase}} -B -e 'show columns in {{exampletable}}' | mlr --itsvlite --ojson --jlistwrap --jvstack cat`

- Retrieve data from an API and pretty print the output:

`curl -s {{http://date.jsontest.com}} | mlr --ijson --opprint cat`
