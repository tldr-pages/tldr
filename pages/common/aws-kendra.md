# aws kendra

> CLI for AWS Kendra.
> More information: <https://docs.aws.amazon.com/cli/latest/reference/kendra/index.html>.

- Create an index:

`aws kendra create-index --name {{name}} --role-arn {{role-arn}}`

- List indexes:

`aws kendra list-indexes`

- Describe an index:

`aws kendra describe-index --id {{index-id}}`

- List data sources:

`aws kendra list-data-sources`

- Describe a data source:

`aws kendra describe-data-source --id {{data-source-id}}`

- List search queries:

`aws kendra list-query-suggestions --index-id {{index-id}} --query-text {{query-text}}`
