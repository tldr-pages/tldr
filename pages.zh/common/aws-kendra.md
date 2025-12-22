# aws kendra

> AWS Kendra 的 CLI。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/kendra/>.

- 创建一个索引：

`aws kendra create-index --name {{名称}} --role-arn {{角色_arn}}`

- 列出索引：

`aws kendra list-indexes`

- 描述一个索引：

`aws kendra describe-index --id {{索引_id}}`

- 列出数据源：

`aws kendra list-data-sources`

- 描述一个数据源：

`aws kendra describe-data-source --id {{数据源_id}}`

- 列出搜索查询建议：

`aws kendra list-query-suggestions --index-id {{索引_id}} --query-text {{查询文本}}`
