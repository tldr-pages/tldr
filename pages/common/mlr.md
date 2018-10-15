# mlr

> Miller is like `awk`, `sed`, `cut`, `join`, and `sort` for name-indexed data such as CSV, TSV, and tabular JSON.

- Pretty-print a CSV file in a tabular format:

`mlr --icsv --opprint cat {{example.csv}}`

- Receive JSON data and pretty print the output:

`echo '{"hello":"world"}' | mlr --ijson --opprint cat`

- Sort alphabetically on field:

`mlr --icsv --opprint sort -f {{field}} {{example.csv}}`

- Sort in descending numerical order on field:

`mlr --icsv --opprint sort -nr {{field}} {{example.csv}}`

- Convert CSV to JSON, performing calculations and display those calculations:

`mlr --icsv --ojson put '${{newField1}} = ${{oldFieldA}}/${{oldFieldB}}' {{example.csv}}`

- Retrieve records from a MySQL database and format the output as vertical JSON:

`mysql --database={{exampledatabase}} -B -e 'show columns in {{exampletable}}' | mlr --itsvlite --ojson --jlistwrap --jvstack cat`
