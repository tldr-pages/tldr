# q

> Execute SQL-like queries on .csv and .tsv files.
> More information: <https://harelba.github.io/q>.

- Query `.csv` file by specifying the delimiter as ',':

`q -d',' "SELECT * from {{path/to/file}}"`

- Query `.tsv` file:

`q -t "SELECT * from {{path/to/file}}"`

- Query file with header row:

`q -d{{delimiter}} -H "SELECT * from {{path/to/file}}"`

- Read data from `stdin`; '-' in the query represents the data from `stdin`:

`{{output}} | q "select * from -"`

- Join two files (aliased as `f1` and `f2` in the example) on column `c1`, a common column:

`q "SELECT * FROM {{path/to/file}} f1 JOIN {{path/to/other_file}} f2 ON (f1.c1 = f2.c1)"`

- Format output using an output delimiter with an output header line (Note: command will output column names based on the input file header or the column aliases overridden in the query):

`q -D{{delimiter}} -O "SELECT {{column}} as {{alias}} from {{path/to/file}}"`
