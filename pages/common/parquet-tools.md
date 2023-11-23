# parquet-tools

> A tool to show, inspect and manipulate Parquet file.
> More information: <https://github.com/apache/parquet-mr>.

- Display the content of a Parquet file:

`parquet-tools cat {{path/to/parquet}}`

- Display the first few lines of a Parquet file:

`parquet-tools head {{path/to/parquet}}`

- Print the schema of a Parquet file:

`parquet-tools schema {{path/to/parquet}}`

- Print the metadata of a Parquet file:

`parquet-tools meta {{path/to/parquet}}`

- Print the content and metadata of a Parquet file:

`parquet-tools dump {{path/to/parquet}}`

- Concatenate several Parquet files into the target one:

`parquet-tools merge {{path/to/parquet1}} {{path/to/parquet2}} {{path/to/target_parquet}}`

- Print the count of rows in a Parquet file:

`parquet-tools rowcount {{path/to/parquet}}`

- Print the column and offset indexes of a Parquet file:

`parquet-tools column-index {{path/to/parquet}}`
