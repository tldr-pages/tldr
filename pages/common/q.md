# q

> Execute SQL-like queries on .csv and .tsv files.

- Query simple .csv file:

`q -d, "SELECT * from {{path/to/file}}"`

- Query simple .tsv file:

`q -t "SELECT * from {{path/to/file}}"`

- Query file with header row:

`q -t -H "SELECT * from {{path/to/file}}"`

- Read data from stdin:

`{{output}} | q "select * from -"`

- Join two files:

`q "SELECT * FROM {{path/to/file}} f1 JOIN {{path/to/other_file}} f2 ON (f1.c1 = f2.c1)"`

- Format output (output delimiter of space) with output header line (note: will output aliased column names):

`q -D" " -O "SELECT * from {{path/to/file}}"`
