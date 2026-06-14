# aws dynamodb

> Շահագործել AWS Dynamodb տվյալների բազան՝ արագ NoSQL տվյալների բազա՝ կանխատեսելի կատարողականությամբ և անխափան մասշտաբայնությամբ:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/dynamodb/>:.

- Ստեղծեք աղյուսակ.:

`aws dynamodb create-table --table-name {{table_name}} --attribute-definitions {{AttributeName=S,AttributeType=S}} --key-schema {{AttributeName=S,KeyType=HASH}} --provisioned-throughput {{ReadCapacityUnits=5,WriteCapacityUnits=5}}`

- Թվարկեք բոլոր աղյուսակները DynamoDB-ում.:

`aws dynamodb list-tables`

- Ստացեք մանրամասներ կոնկրետ աղյուսակի մասին.:

`aws dynamodb describe-table --table-name {{table_name}}`

- Ավելացրեք տարր աղյուսակում.:

`aws dynamodb put-item --table-name {{table_name}} --item '{{{"AttributeName": {"S": "value"}}}}'`

- Առբերեք նյութը աղյուսակից.:

`aws dynamodb get-item --table-name {{table_name}} --key '{{{"ID": {"N": "1"}}}}'`

- Թարմացրեք աղյուսակի որևէ կետ.:

`aws dynamodb update-item --table-name {{table_name}} --key '{{{"ID": {"N": "1"}}}}' --update-expression "{{SET Name = :n}}" --expression-attribute-values '{{{":n": {"S": "Jane"}}}}'`

- Սկանավորեք աղյուսակի տարրերը.:

`aws dynamodb scan --table-name {{table_name}}`

- Ջնջել տարրը աղյուսակից.:

`aws dynamodb delete-item --table-name {{table_name}} --key '{{{"ID": {"N": "1"}}}}'`
