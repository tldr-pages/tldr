# aws kendra

> AWS Kendra 的命令行界面。
> 更多信息：<https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/index.html>.

- 创建索引：

`aws kendra create-index --name {{name}} --role-arn {{role_arn}}`

- 列出索引：

`aws kendra list-indexes`

- 描述索引：

`aws kendra describe-index --id {{index_id}}`

- 列出数据源：

`aws kendra list-data-sources`

- 描述数据源：

`aws kendra describe-data-source --id {{data_source_id}}`

- 列出搜索查询建议：

`aws kendra list-query-suggestions --index-id {{index_id}} --query-text {{query_text}}`
