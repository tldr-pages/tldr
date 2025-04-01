# gcloud sql export sql

> 将数据从 Cloud SQL 实例导出到 Google Cloud 存储桶中的 SQL 文件。
> 用于创建备份或迁移数据。有关更多信息，请参阅：`gcloud`。
> 更多信息：<https://cloud.google.com/sdk/gcloud/reference/sql/export/sql>.

- 将数据从特定的 Cloud SQL 实例导出到 Google Cloud 存储桶中的 SQL 数据转储文件：

`gcloud sql export sql {{instance}} gs://{{bucket_name}}/{{file_name}}`

- 异步导出数据，立即返回而不等待操作完成：

`gcloud sql export sql {{instance}} gs://{{bucket_name}}/{{file_name}} --async`

- 从 Cloud SQL 实例中的特定数据库导出数据：

`gcloud sql export sql {{instance}} gs://{{bucket_name}}/{{file_name}} --database={{database1,database2,...}}`

- 从 Cloud SQL 实例中指定的数据库导出特定表：

`gcloud sql export sql {{instance}} gs://{{bucket_name}}/{{file_name}} --database={{database}} --table={{table1,table2,...}}`

- 在导出数据时将操作转移到临时实例以减少对源实例的压力：

`gcloud sql export sql {{instance}} gs://{{bucket_name}}/{{file_name}} --offload`

- 导出数据并使用 `gzip` 压缩输出：

`gcloud sql export sql {{instance}} gs://{{bucket_name}}/{{file_name}}.gz`
