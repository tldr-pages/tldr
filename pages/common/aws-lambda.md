# aws lambda

> CLI for AWS lambda.
> More information: <https://docs.aws.amazon.com/cli/latest/reference/lambda/index.html>.

- Run a function:

`aws lambda invoke --function-name {{function_name}} {{local_file_to_store_results}}`

- Run a function with payload as input:

`aws lambda invoke --function-name {{function_name}} --payload {{payload_in_json}} {{local_file_to_store_results}}`

- List functions:

`aws lambda list-functions`

- Get function configuration:

`aws lambda get-function-configuration --function-name  {{function_name}}`

- List function aliases:

`aws lambda list-aliases --function-name {{function_name}}`

- Get function reserved concurrency:

`aws lambda get-function-concurrency --function-name {{function_name}}`

- List which AWS services can invoke the function:

`aws lambda get-policy --function-name {{function_name}}`
