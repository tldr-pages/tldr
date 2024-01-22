# bq

> A Python-based tool for BigQuery.
> More information: <https://cloud.google.com/bigquery/docs/reference/bq-cli-reference>.

- Run query against a BigQuery table using standard SQL, add `--dry_run` flag to estimate the number of bytes read by the query:

`bq query --nouse_legacy_sql 'SELECT COUNT(*) FROM {{DATASET_NAME}}.{{TABLE_NAME}}'`

- Run a parameterized query:

`bq query --use_legacy_sql=false --parameter='ts_value:TIMESTAMP:2016-12-07 08:00:00' 'SELECT TIMESTAMP_ADD(@ts_value, INTERVAL 1 HOUR)'`

- Create a new dataset or table in the US location:

`bq mk --location=US {{dataset_name}}.{{table_name}}`

- List all datasets in a project:

`bq ls --filter labels.{{key}}:{{value}} --max_results {{integer}} --format=prettyjson --project_id {{project_id}}`

- Batch load data from a specific file in formats such as CSV, JSON, Parquet, and Avro to a table:

`bq load --location={{location}} --source_format={{CSV|JSON|PARQUET|AVRO}} {{dataset}}.{{table}} {{path_to_source}}`

- Copy one table to another:

`bq cp {{dataset}}.{{OLD_TABLE}} {{dataset}}.{{new_table}}`

- Display help:

`bq help`
