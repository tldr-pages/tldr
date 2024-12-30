# bq

> 一个基于Python的工具，用于BigQuery，谷歌云的完全托管和完全无服务器的企业数据仓库。
> 更多信息：<https://cloud.google.com/bigquery/docs/reference/bq-cli-reference>。

- 使用标准SQL针对BigQuery表运行查询，添加`--dry_run`标志以估算查询读取的字节数：

`bq query --nouse_legacy_sql 'SELECT COUNT(*) FROM {{DATASET_NAME}}.{{TABLE_NAME}}'`

- 运行参数化查询：

`bq query --use_legacy_sql=false --parameter='ts_value:TIMESTAMP:2016-12-07 08:00:00' 'SELECT TIMESTAMP_ADD(@ts_value, INTERVAL 1 HOUR)'`

- 在美国地区创建新的数据集或表：

`bq mk --location=US {{dataset_name}}.{{table_name}}`

- 列出项目中的所有数据集：

`bq ls --filter labels.{{key}}:{{value}} --max_results {{integer}} --format=prettyjson --project_id {{project_id}}`

- 从特定文件批量加载数据，支持CSV、JSON、Parquet和Avro等格式到表中：

`bq load --location {{location}} --source_format {{CSV|JSON|PARQUET|AVRO}} {{dataset}}.{{table}} {{path_to_source}}`

- 将一个表复制到另一个表：

`bq cp {{dataset}}.{{OLD_TABLE}} {{dataset}}.{{new_table}}`

- 显示帮助信息：

`bq help`