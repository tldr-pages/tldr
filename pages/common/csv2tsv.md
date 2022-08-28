# csv2tsv

> Convert CSV (comma-separated) text to TSV (tab-separated) format.
> More information: <https://github.com/eBay/tsv-utils/blob/master/README.md#csv2tsv>.

- Convert from CSV to TSV:

`csv2tsv {{path/to/input_csv1 path/to/input_csv2 ...}} > {{path/to/output_tsv}}`

- Convert field delimiter separated CSV to TSV:

`csv2tsv -c'{{field_delimiter}}' {{path/to/input_csv}}`

- Convert semicolon separated CSV to TSV:

`csv2tsv -c';' {{path/to/input_csv}}`
