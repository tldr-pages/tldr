# gcloud logging logs list

> 列出 Google Cloud 项目中的日志。
> 对于监测和分析可帮助识别可用日志。另见: `gcloud`。
> 更多信息：<https://cloud.google.com/sdk/gcloud/reference/logging/logs/list>。

- 列出当前项目中的所有日志：

`gcloud logging logs list`

- 列出指定日志桶和位置中的所有日志：

`gcloud logging logs list --bucket={{bucket_id}} --location={{location}}`

- 列出指定视图和日志桶中的所有日志：

`gcloud logging logs list --bucket={{bucket_id}} --location={{location}} --view={{view_id}}`

- 使用过滤表达式列出日志：

`gcloud logging logs list --filter="{{expression}}"`

- 列出指定数量的日志：

`gcloud logging logs list --limit={{number}}`

- 按特定字段升序或降序（`~` 为降序）排序日志：

`gcloud logging logs list --sort-by="{{field_name}}"`

- 按多个字段排序日志：

`gcloud logging logs list --sort-by="{{field1}},~{{field2}}"`

- 使用详细输出列出日志，显示额外信息：

`gcloud logging logs list --verbosity=debug`