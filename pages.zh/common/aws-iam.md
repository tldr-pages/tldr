# aws iam

> 与 Identity and Access Management（IAM）交互，这是一个用于安全控制对 AWS 服务访问的 Web 服务。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/iam/>.

- 列出用户：

`aws iam list-users`

- 列出策略：

`aws iam list-policies`

- 列出组：

`aws iam list-groups`

- 获取某个组中的用户：

`aws iam get-group --group-name {{组名}}`

- 描述一个 IAM 策略：

`aws iam get-policy --policy-arn arn:aws:iam::aws:policy/{{策略名称}}`

- 列出访问密钥：

`aws iam list-access-keys`

- 列出某个特定用户的访问密钥：

`aws iam list-access-keys --user-name {{用户名}}`

- 显示帮助：

`aws iam help`
