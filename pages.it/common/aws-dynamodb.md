# aws dynamodb

> Manipola un database AWS DynamoDB, un database NoSQL veloce con prestazioni prevedibili e scalabilità senza soluzione di continuità.
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/dynamodb/>.

- Crea una tabella:

`aws dynamodb create-table --table-name {{nome_table}} --attribute-definitions {{AttributeName=S,AttributeType=S}} --key-schema {{AttributeName=S,KeyType=HASH}} --provisioned-throughput {{ReadCapacityUnits=5,WriteCapacityUnits=5}}`

- Elenca tutte le tabelle in DynamoDB:

`aws dynamodb list-tables`

- Ottieni dettagli su una tabella specifica:

`aws dynamodb describe-table --table-name {{nome_table}}`

- Aggiunge un elemento a una tabella:

`aws dynamodb put-item --table-name {{nome_table}} --item '{{{"AttributeName": {"S": "valore"}}}}'`

- Recupera un elemento da una tabella:

`aws dynamodb get-item --table-name {{nome_table}} --key '{{{"ID": {"N": "1"}}}}'`

- Aggiorna un elemento nella tabella:

`aws dynamodb update-item --table-name {{nome_table}} --key '{{{"ID": {"N": "1"}}}}' --update-expression "{{SET Name = :n}}" --expression-attribute-values '{{{":n": {"S": "Jane"}}}}'`

- Scansiona gli elementi nella tabella:

`aws dynamodb scan --table-name {{nome_table}}`

- Elimina un elemento dalla tabella:

`aws dynamodb delete-item --table-name {{nome_table}} --key '{{{"ID": {"N": "1"}}}}'`
