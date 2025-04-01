# bq

> 一个基于 Python 的 BigQuery 工具，BigQuery 是 Google Cloud 提供的完全托管且完全无服务器的企业级数据仓库。
> 更多信息：<https://cloud.google.com/bigquery/docs/reference/bq-cli-reference>.

- 使用标准 SQL 对 BigQuery 表执行查询，添加 `--dry_run` 标志来估算查询读取的字节数：

`bq query --nouse_legacy_sql 'SELECT COUNT(*) FROM {{DATASET_NAME}}.{{TABLE_NAME}}'`

- 运行参数化查询：

`bq query --use_legacy_sql=false --parameter='ts_value:TIMESTAMP:2016-12-07 08:00:00' 'SELECT TIMESTAMP_ADD(@ts_value, INTERVAL 1 HOUR)'`

- 在 US 位置创建新数据集或表：

`bq mk --location=US {{dataset_name}}.{{table_name}}`

- 列出项目中的所有数据集：

`bq ls --filter labels.{{key}}:{{value}} --max_results {{integer}} --format=prettyjson --project_id {{project_id}}`

- 从特定文件批量加载 CSV、JSON、Parquet 和 Avro 等格式的数据到表中：

`bq load --location {{location}} --source_format {{CSV|JSON|PARQUET|AVRO}} {{dataset}}.{{table}} {{path_to_source}}`

- 复制一个表到另一个表：

`bq cp {{dataset}}.{{OLD_TABLE}} {{dataset}}.{{new_table}}`

- 显示帮助：

`bq help`