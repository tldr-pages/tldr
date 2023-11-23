# aws dynamodb

> CLI for AWS dynamodb.
> More information: <https://docs.aws.amazon.com/cli/latest/reference/dynamodb/>.

- Create a table:

`aws dynamodb create-table --table-name {{TableName}} --attribute-definitions AttributeName=S,AttributeType=S --key-schema AttributeName=S,KeyType=HASH --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5`

- List all tables in the DynamoDB:

`aws dynamodb list-tables`

- Get details about a specific table:

`aws dynamodb describe-table --table-name {{TableName}}`

- Add an item to a table:

`aws dynamodb put-item --table-name {{TableName}} --item '{"AttributeName": {"S": "value"}}'`

- Retrieve an item from a table:

`aws dynamodb get-item \ --table-name {{TableName}} \ --key '{"ID": {"N": "1"}}'`

- Update an item in the table:

`aws dynamodb update-item --table-name {{TableName}} --key '{"ID": {"N": "1"}}' --update-expression "SET Name = :n" --expression-attribute-values '{":n": {"S": "Jane"}}'`

- Scan items in the table:

`aws dynamodb scan --table-name {{TableName}}`

- Delete an item from the table:

`aws dynamodb delete-item --table-name {{TableName}} --key '{"ID": {"N": "1"}}'`
