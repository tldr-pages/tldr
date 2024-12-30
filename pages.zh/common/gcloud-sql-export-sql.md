# gcloud sql 导出 sql

> 从 Cloud SQL 实例导出数据到 Google Cloud Storage 中的 SQL 文件。
> 对于创建备份或迁移数据非常有用。另见：`gcloud`。
> 更多信息：<https://cloud.google.com/sdk/gcloud/reference/sql/export/sql>。

- 将数据从特定的 Cloud SQL 实例导出到 Google Cloud Storage 存储桶，作为 SQL 转储文件：

`gcloud sql export sql {{instance}} gs://{{bucket_name}}/{{file_name}}`

- 异步导出数据，立即返回而不等待操作完成：

`gcloud sql export sql {{instance}} gs://{{bucket_name}}/{{file_name}} --async`

- 从 Cloud SQL 实例中特定的数据库导出数据：

`gcloud sql export sql {{instance}} gs://{{bucket_name}}/{{file_name}} --database={{database1,database2,...}}`

- 从 Cloud SQL 实例中特定数据库导出特定表的数据：

`gcloud sql export sql {{instance}} gs://{{bucket_name}}/{{file_name}} --database={{database}} --table={{table1,table2,...}}`

- 在导出数据时将操作转移到临时实例，以减少对源实例的压力：

`gcloud sql export sql {{instance}} gs://{{bucket_name}}/{{file_name}} --offload`

- 导出数据并使用 `gzip` 压缩输出：

`gcloud sql export sql {{instance}} gs://{{bucket_name}}/{{file_name}}.gz`