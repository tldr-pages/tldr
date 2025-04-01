# cradle elastic

> 管理 Cradle 实例的 Elasticsearch 实例。
> 更多信息：<https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#elastic>.

- 清空 Elasticsearch 索引：

`cradle elastic flush`

- 清空特定包的 Elasticsearch 索引：

`cradle elastic flush {{package}}`

- 提交 Elasticsearch 模式：

`cradle elastic map`

- 提交特定包的 Elasticsearch 模式：

`cradle elastic map {{package}}`

- 为所有包填充 Elasticsearch 索引：

`cradle elastic populate`

- 为特定包填充 Elasticsearch 索引：

`cradle elastic populate {{package}}`
