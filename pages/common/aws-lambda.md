# aws lambda

> CLI for AWS lambda.
> More information: <https://docs.aws.amazon.com/cli/latest/reference/lambda/index.html>.

- Run a function:

`aws lambda invoke --function-name {{name}} {{path/to/response}}.json`

- Run a function with an input payload in JSON format:

`aws lambda invoke --function-name {{name}} --payload {{json}} {{path/to/response}}.json`

- List functions:

`aws lambda list-functions`

- Display the configuration of a function:

`aws lambda get-function-configuration --function-name {{name}}`

- List function aliases:

`aws lambda list-aliases --function-name {{name}}`

- Display the reserved concurrency configuration for a function:

`aws lambda get-function-concurrency --function-name {{name}}`

- List which AWS services can invoke the function:

`aws lambda get-policy --function-name {{name}}`
