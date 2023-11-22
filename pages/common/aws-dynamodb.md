# aws dynamodb

> CLI for AWS IAM.
> More information: <https://docs.aws.amazon.com/cli/latest/reference/dynamodb/>.

- Create a table:

`aws dynamodb create-table --table-name TableName --attribute-definitions AttributeName=S,AttributeType=S --key-schema AttributeName=S,KeyType=HASH --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5`

- To list all tables in your DynamoDB, you can use the `list-tables` command:

`aws dynamodb list-tables`

- To get details about a specific table, you can use the `describe-table` command:

`aws dynamodb describe-table --table-name MyTable`

- To add an item to a table, you use the `put-item` command:

`aws dynamodb put-item --table-name TableName --item '{"AttributeName": {"S": "value"}}'`

- To retrieve an item from a table, you use the `get-item`command:

`aws dynamodb get-item \ --table-name MyTable \ --key '{"ID": {"N": "1"}}'`

- To Update an Item in the Table, you can use `update-item` command:

`aws dynamodb update-item --table-name MyTable --key '{"ID": {"N": "1"}}' --update-expression "SET Name = :n" --expression-attribute-values '{":n": {"S": "Jane"}}'`

- To Scan Items in the Table, you can use `scan` command:

`aws dynamodb scan --table-name MyTable`

- To Delete an Item from the Table, you can use `delete-item` command:

`aws dynamodb delete-item --table-name MyTable --key '{"ID": {"N": "1"}}'`
