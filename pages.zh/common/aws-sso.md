# aws sso

> 使用 Single Sign-On (SSO) 凭证管理对 AWS 资源的访问。
> 更多信息：<https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso/index.html>.

- 开始 SSO 会话并刷新访问令牌。需要使用 `aws configure sso` 进行设置：

`aws sso login`

- 结束 SSO 会话并清除缓存的访问令牌：

`aws sso logout`

- 列出用户可访问的所有 AWS 账户：

`aws sso list-accounts`

- 列出用户对于指定 AWS 账户可访问的所有角色：

`aws sso list-account-roles --account-id {{account}} --access-token {{token}}`

- 获取特定账户的短期凭证：

`aws get-role-credentials --account-id {{account}} --role-name {{role}} --access-token {{token}}`