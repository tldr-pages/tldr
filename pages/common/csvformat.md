# csvformat

> Convert a CSV file to a custom output format.
> Included in csvkit.
> More information: <https://csvkit.readthedocs.io/en/latest/scripts/csvformat.html>.

- Convert to a tab-delimited file (TSV):

`csvformat -T {{data.csv}}`

- Convert delimiters to a custom character:

`csvformat -D "{{custom_character}}" {{data.csv}}`

- Convert line endings to carriage return (^M) + line feed:

`csvformat -M "{{\r\n}}" {{data.csv}}`

- Minimize use of quote characters:

`csvformat -U 0 {{data.csv}}`

- Maximize use of quote characters:

`csvformat -U 1 {{data.csv}}`
