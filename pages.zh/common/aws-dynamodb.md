# aws dynamodb

> 操作 AWS DynamoDB 数据库，这是一个快速的 NoSQL 数据库，具有可预测的性能和无缝的可扩展性。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/dynamodb/>。

- 创建一个表：

`aws dynamodb create-table --table-name {{table_name}} --attribute-definitions {{AttributeName=S,AttributeType=S}} --key-schema {{AttributeName=S,KeyType=HASH}} --provisioned-throughput {{ReadCapacityUnits=5,WriteCapacityUnits=5}}`

- 列出 DynamoDB 中的所有表：

`aws dynamodb list-tables`

- 获取特定表的详细信息：

`aws dynamodb describe-table --table-name {{table_name}}`

- 向表中添加一个项：

`aws dynamodb put-item --table-name {{table_name}} --item '{{{"AttributeName": {"S": "value"}}}}'`

- 从表中检索一个项：

`aws dynamodb get-item --table-name {{table_name}} --key '{{{"ID": {"N": "1"}}}}'`

- 更新表中的一项：

`aws dynamodb update-item --table-name {{table_name}} --key '{{{"ID": {"N": "1"}}}}' --update-expression "{{SET Name = :n}}" --expression-attribute-values '{{{":n": {"S": "Jane"}}}}'`

- 扫描表中的项：

`aws dynamodb scan --table-name {{table_name}}`

- 从表中删除一个项：

`aws dynamodb delete-item --table-name {{table_name}} --key '{{{"ID": {"N": "1"}}}}'`