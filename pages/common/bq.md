# bq

> The bq command-line tool is a Python-based command-line tool for BigQuery.
> More information: <https://cloud.google.com/bigquery/docs/reference/bq-cli-reference>.

- Run query against a BigQuery table using standard SQL, add the `--dry_run` flag to estimate the number of bytes read by the query:

`bq query --nouse_legacy_sql 'SELECT COUNT(*) FROM {{DATASET_NAME}}.{{TABLE_NAME}}'`

- Run a specific parameterized query:

`bq query --use_legacy_sql=false --parameter='ts_value:TIMESTAMP:2016-12-07 08:00:00' 'SELECT TIMESTAMP_ADD(@ts_value, INTERVAL 1 HOUR)'`

- Create a new dataset or table in the US location:

`bq mk --location=US {{DATASET_NAME}}.{{TABLE_NAME}}`

- List all datasets in a project:

`bq ls --filter labels.{{KEY}}:{{VALUE}} --max_results {{INTEGER}} --format=prettyjson --project_id {{PROJECT_ID}}`

- Batch load data from a specific file in formats such as CSV, JSON, Parquet, and Avro to a table:

`bq load --location={{LOCATION}} --source_format={{FORMAT}} {{DATASET}}.{{TABLE}} {{PATH_TO_SOURCE}}`

- Copy one table to another:

`bq cp {{DATASET}}.{{OLD_TABLE}} {{DATASET}}.{{NEW_TABLE}}`

- Get help:

`bq help`
