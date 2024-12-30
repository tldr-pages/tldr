# aws secretsmanager

> 存储、管理和检索秘密。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/secretsmanager/>.

- 显示当前账户中由秘密管理器存储的秘密：

`aws secretsmanager list-secrets`

- 列出所有秘密，但仅显示秘密名称和 ARN（易于查看）：

`aws secretsmanager list-secrets --query 'SecretList[*].{Name: Name, ARN: ARN}'`

- 创建一个秘密：

`aws secretsmanager create-secret --name {{name}} --description "{{secret_description}}" --secret-string '{{secret}}'`

- 删除一个秘密（附加 `--force-delete-without-recovery` 以立即删除而不进行任何恢复）：

`aws secretsmanager delete-secret --secret-id {{name|arn}}`

- 查看一个秘密的详细信息，但不包括秘密文本：

`aws secretsmanager describe-secret --secret-id {{name|arn}}`

- 检索一个秘密的值（要获取最新版本的秘密，请省略 `--version-stage`）：

`aws secretsmanager get-secret-value --secret-id {{name|arn}} --version-stage {{version_of_secret}}`

- 使用 Lambda 函数立即旋转秘密：

`aws secretsmanager rotate-secret --secret-id {{name|arn}} --rotation-lambda-arn {{arn_of_lambda_function}}`

- 使用 Lambda 函数每 30 天自动旋转秘密：

`aws secretsmanager rotate-secret --secret-id {{name|arn}} --rotation-lambda-arn {{arn_of_lambda_function}} --rotation-rules AutomaticallyAfterDays={{30}}`