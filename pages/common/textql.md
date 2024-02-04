# textql

> Execute SQL against structured text like csv or tsv files.
> More information: <https://github.com/dinedal/textql>.

- Print the lines in the specified `.csv` file that match a SQL query to `stdout`:

`textql -sql "{{SELECT * FROM filename}}" {{path/to/filename.csv}}`

- Query `.tsv` file:

`textql -dlm=tab -sql "{{SELECT * FROM filename}}" {{path/to/filename.tsv}}`

- Query file with header row:

`textql -dlm={{delimiter}} -header -sql "{{SELECT * FROM filename}}" {{path/to/filename.csv}}`

- Read data from `stdin`:

`cat {{path/to/file}} | textql -sql "{{SELECT * FROM stdin}}"`

- Join two files on a specified common column:

`textql -header -sql "SELECT * FROM {{path/to/file1}} JOIN {{file2}} ON {{path/to/file1}}.{{c1}} = {{file2}}.{{c1}} LIMIT {{10}}" -output-header {{path/to/file1.csv}} {{path/to/file2.csv}}`

- Format output using an output delimiter with an output header line:

`textql -output-dlm={{delimiter}} -output-header -sql "SELECT {{column}} AS {{alias}} FROM {{filename}}" {{path/to/filename.csv}}`
