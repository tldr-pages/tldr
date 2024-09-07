# aws kendra

> CLI for AWS Kendra.
> More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/index.html>.

- Create an index:

`aws kendra create-index --name {{name}} --role-arn {{role_arn}}`

- List indexes:

`aws kendra list-indexes`

- Describe an index:

`aws kendra describe-index --id {{index_id}}`

- List data sources:

`aws kendra list-data-sources`

- Describe a data source:

`aws kendra describe-data-source --id {{data_source_id}}`

- List search queries:

`aws kendra list-query-suggestions --index-id {{index_id}} --query-text {{query_text}}`
