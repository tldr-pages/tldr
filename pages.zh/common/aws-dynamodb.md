# aws dynamodb

> 操作 AWS DynamoDB 数据库，这是一个具有可预测性能和无缝扩展能力的快速 NoSQL 数据库。
> 更多信息： <https://docs.aws.amazon.com/cli/latest/reference/dynamodb/>.

- 创建一个表：

`aws dynamodb create-table --table-name {{表名}} --attribute-definitions {{属性名=S,属性类型=S}} --key-schema {{属性名=S,键类型=HASH}} --provisioned-throughput {{读取容量单位=5,写入容量单位=5}}`

- 列出 DynamoDB 中的所有表：

`aws dynamodb list-tables`

- 获取指定表的详细信息：

`aws dynamodb describe-table --table-name {{表名}}`

- 向表中添加一个项目：

`aws dynamodb put-item --table-name {{表名}} --item '{{{"AttributeName": {"S": "value"}}}}'`

- 从表中检索一个项目：

`aws dynamodb get-item --table-name {{表名}} --key '{{{"ID": {"N": "1"}}}}'`

- 更新表中的一个项目：

`aws dynamodb update-item --table-name {{表名}} --key '{{{"ID": {"N": "1"}}}}' --update-expression "{{SET Name = :n}}" --expression-attribute-values '{{{":n": {"S": "Jane"}}}}'`

- 扫描表中的项目：

`aws dynamodb scan --table-name {{表名}}`

- 从表中删除一个项目：

`aws dynamodb delete-item --table-name {{表名}} --key '{{{"ID": {"N": "1"}}}}'`
