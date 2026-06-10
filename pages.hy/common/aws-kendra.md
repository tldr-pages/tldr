# aws kendra

> CLI AWS Kendra-ի համար:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/kendra/>:.

- Ստեղծեք ինդեքս.:

`aws kendra create-index --name {{name}} --role-arn {{role_arn}}`

- Ցանկի ինդեքսները.:

`aws kendra list-indexes`

- Նկարագրեք ինդեքսը.:

`aws kendra describe-index --id {{index_id}}`

- Թվարկեք տվյալների աղբյուրները.:

`aws kendra list-data-sources`

- Նկարագրեք տվյալների աղբյուրը.:

`aws kendra describe-data-source --id {{data_source_id}}`

- Ցանկի որոնման հարցումները.:

`aws kendra list-query-suggestions --index-id {{index_id}} --query-text {{query_text}}`
