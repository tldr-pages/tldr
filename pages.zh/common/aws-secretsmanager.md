# aws secretsmanager

> 存储、管理和检索密钥。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/secretsmanager/>。

- 显示当前账户中由密钥管理器存储的密钥：

`aws secretsmanager list-secrets`

- 列出所有密钥，但仅显示密钥名称和 ARN（便于查看）：

`aws secretsmanager list-secrets --query 'SecretList[*].{Name: Name, ARN: ARN}'`

- 创建一个密钥：

`aws secretsmanager create-secret --name {{name}} --description "{{secret_description}}" --secret-string '{{secret}}'`

- 删除一个密钥（添加 `--force-delete-without-recovery` 以立即删除而无需恢复期）：

`aws secretsmanager delete-secret --secret-id {{name|arn}}`

- 查看密钥的详细信息，但不包括密钥文本：

`aws secretsmanager describe-secret --secret-id {{name|arn}}`

- 检索密钥的值（要获取密钥的最新版本，可以省略 `--version-stage`）：

`aws secretsmanager get-secret-value --secret-id {{name|arn}} --version-stage {{version_of_secret}}`

- 立即使用 Lambda 函数轮换密钥：

`aws secretsmanager rotate-secret --secret-id {{name|arn}} --rotation-lambda-arn {{arn_of_lambda_function}}`

- 使用 Lambda 函数每 30 天自动轮换密钥：

`aws secretsmanager rotate-secret --secret-id {{name|arn}} --rotation-lambda-arn {{arn_of_lambda_function}} --rotation-rules AutomaticallyAfterDays={{30}}`
