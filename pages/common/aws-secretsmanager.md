# aws secretsmanager

> Store, manage, and retrieve secrets.
> More information: <https://docs.aws.amazon.com/cli/latest/reference/secretsmanager/>.

- Show secrets stored by the secrets manager in the current account:

`aws secretsmanager list-secrets`

- Create a secret:

`aws secretsmanager create-secret --name {{name}} --description "{{secret_description}}" --secret-string {{secret}}`

- Delete a secret:

`aws secretsmanager delete-secret --secret-id {{name_or_arn}}`

- View details of a secret except for secret text:

`aws secretsmanager describe-secret --secret-id {{name_or_arn}}`

- Retrieve the value of a secret (to get the latest version of the secret omit `--version-stage`):

`aws secretsmanager get-secret-value --secret-id {{name_or_arn}} --version-stage {{version_of_secret}}`

- Rotate the secret immediately using a Lambda function:

`aws secretsmanager rotate-secret --secret-id {{name_or_arn}} --rotation-lambda-arn {{arn_of_lambda_function}}`

- Rotate the secret automatically every 30 days using a Lambda function:

`aws secretsmanager rotate-secret --secret-id {{name_or_arn}} --rotation-lambda-arn {{arn_of_lambda_function}} --rotation-rules AutomaticallyAfterDays={{30}}`
