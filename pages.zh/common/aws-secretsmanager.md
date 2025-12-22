# aws secretsmanager

> 存储、管理和检索密钥。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/secretsmanager/>.

- 显示当前账户中由 Secrets Manager 存储的密钥：

`aws secretsmanager list-secrets`

- 列出所有密钥，但只显示密钥名称和 ARN（便于查看）：

`aws secretsmanager list-secrets --query 'SecretList[*].{Name: Name, ARN: ARN}'`

- 创建一个密钥：

`aws secretsmanager create-secret --name {{名称}} --description "{{密钥描述}}" --secret-string '{{密钥}}'`

- 删除一个密钥（附加 `--force-delete-without-recovery` 可立即删除且不经过任何恢复期）：

`aws secretsmanager delete-secret --secret-id {{名称|arn}}`

- 查看密钥的详细信息，但不包含密钥内容：

`aws secretsmanager describe-secret --secret-id {{名称|arn}}`

- 获取密钥的值（若要获取密钥的最新版本，可省略 `--version-stage`）：

`aws secretsmanager get-secret-value --secret-id {{名称|arn}} --version-stage {{密钥版本}}`

- 使用 Lambda 函数立即轮换密钥：

`aws secretsmanager rotate-secret --secret-id {{名称|arn}} --rotation-lambda-arn {{Lambda_函数的_arn}}`

- 使用 Lambda 函数每 30 天自动轮换一次密钥：

`aws secretsmanager rotate-secret --secret-id {{名称|arn}} --rotation-lambda-arn {{Lambda_函数的_arn}} --rotation-rules AutomaticallyAfterDays={{30}}`
