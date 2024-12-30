# gcloud 日志 列表

> 列出 Google Cloud 项目中的日志。
> 有助于识别可用于监控和分析的日志。另见：`gcloud`。
> 更多信息：<https://cloud.google.com/sdk/gcloud/reference/logging/logs/list>。

- 列出当前项目中的所有日志：

`gcloud logging logs list`

- 列出特定日志桶和位置的所有日志：

`gcloud logging logs list --bucket={{bucket_id}} --location={{location}}`

- 列出日志桶中特定视图的所有日志：

`gcloud logging logs list --bucket={{bucket_id}} --location={{location}} --view={{view_id}}`

- 列出带有过滤表达式的日志：

`gcloud logging logs list --filter="{{expression}}"`

- 列出指定数量的日志：

`gcloud logging logs list --limit={{number}}`

- 按特定字段升序或降序排序日志（`~` 表示降序）：

`gcloud logging logs list --sort-by="{{field_name}}"`

- 按多个字段排序日志：

`gcloud logging logs list --sort-by="{{field1}},~{{field2}}"`

- 列出带有详细输出的日志，显示额外的细节：

`gcloud logging logs list --verbosity=debug`