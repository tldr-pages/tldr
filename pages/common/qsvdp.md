# qsvdp

> Slimmed-down build of `qsv` optimized for CKAN and Datapusher+, bundling Polars and Luau.
> Most commands also exist in `qsv` proper; this page focuses on those commonly used with `qsvdp`.
> See also: `qsv`, `qsvlite`.
> More information: <https://github.com/dathere/qsv>.

- Hash a CSV file with BLAKE3:

`qsv blake3 {{path/to/file.csv}}`

- Detect delimiter, encoding, column types, etc.:

`qsvdp sniff {{path/to/file.csv}}`

- Validate against a JSON Schema:

`qsvdp validate {{path/to/file.csv}} {{path/to/schema.json}}`

- Run SQL using Polars (files are aliased as `_t_1`, `_t_2`, etc):

`qsvdp sqlp {{path/to/file.csv}} '{{SELECT * FROM _t_1 LIMIT 10}}'`

- Add a new computed column using Luau:

`qsvdp luau map {{new_column}} '{{return old_column * 2}}' {{path/to/file.csv}}`
