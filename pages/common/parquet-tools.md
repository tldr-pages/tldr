# parquet-tools

> A tool to show, inspect and manipulate Parquet file.
> More information: <https://github.com/apache/parquet-mr/tree/master/parquet-tools>.

- Prints the content of a Parquet file.

`parquet-tools cat {{path/to/parquet}}`

- Prints the first n record of the Parquet file.

`parquet-tools head {{path/to/parquet}}`

- Prints the schema of Parquet file(s).

`parquet-tools schema {{path/to/parquet}}`

- Prints the metadata of Parquet file(s).

`parquet-tools meta {{path/to/parquet}}`

- Prints the content and metadata of a Parquet file

`parquet-tools dump {{path/to/parquet}}`

- Merges multiple Parquet files into one.

`parquet-tools merge {{path/to/input_parquet_1}} {{path/to/input_parquet_2}} {{path/to/output_parquet}}`

- Prints the count of rows in Parquet file(s).

`parquet-tools rowcount {{path/to/parquet}}`

- Prints the size of Parquet file(s).

`parquet-tools size {{path/to/parquet}}`

- Prints the column and offset indexes of a Parquet file.

`parquet-tools column-index {{path/to/parquet}}`
