# qo

> Query JSON, CSV, TSV, and PSV files using SQL.
> Each file argument becomes a table named after the file; piped input becomes the table `tmp`.
> More information: <https://github.com/kiki-ki/go-qo>.

- Explore one or more files in the interactive interface:

`qo {{path/to/data.json}}`

- Run a query against a file and print the result:

`qo {{[-q|--query]}} "{{SELECT * FROM data}}" {{path/to/data.json}}`

- Run a query against piped input:

`{{command}} | qo {{[-q|--query]}} "{{SELECT * FROM tmp}}"`

- Join two files in a single query:

`qo {{[-q|--query]}} "{{SELECT * FROM x JOIN y ON x.id = y.x_id}}" {{path/to/x.json}} {{path/to/y.json}}`

- Read a specific input format and write a specific output format:

`qo {{[-i|--input]}} {{csv}} {{[-o|--output]}} {{json|jsonl|csv|tsv|psv|table}} {{[-q|--query]}} "{{SELECT * FROM users}}" {{path/to/users.csv}}`

- Treat the first row of a delimited file as data instead of as a header:

`qo {{[-i|--input]}} csv --no-header {{[-q|--query]}} "{{SELECT col1, col2 FROM raw}}" {{path/to/raw.csv}}`

- Display help:

`qo {{[-h|--help]}}`

- Display version:

`qo {{[-v|--version]}}`
