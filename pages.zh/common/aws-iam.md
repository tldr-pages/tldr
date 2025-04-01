# aws iam

> 与身份和访问管理（IAM）互动，IAM 是一项用于安全控制访问 AWS 服务的网络服务。
> 更多信息：<https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/index.html>。

- 列出用户：

`aws iam list-users`

- 列出策略：

`aws iam list-policies`

- 列出组：

`aws iam list-groups`

- 获取组中的用户：

`aws iam get-group --group-name {{group_name}}`

- 描述 IAM 策略：

`aws iam get-policy --policy-arn arn:aws:iam::aws:policy/{{policy_name}}`

- 列出访问密钥：

`aws iam list-access-keys`

- 列出特定用户的访问密钥：

`aws iam list-access-keys --user-name {{user_name}}`

- 显示帮助：

`aws iam help`