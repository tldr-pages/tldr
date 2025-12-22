# aws sso

> 使用单点登录（SSO）凭据管理对 AWS 资源的访问。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/sso/>.

- 启动 SSO 会话并刷新访问令牌。需要先使用 `aws configure sso` 进行设置：

`aws sso login`

- 结束 SSO 会话并清除缓存的访问令牌：

`aws sso logout`

- 列出用户可访问的所有 AWS 账户：

`aws sso list-accounts`

- 列出用户在指定 AWS 账户中可访问的所有角色：

`aws sso list-account-roles --account-id {{账户}} --access-token {{令牌}}`

- 为指定账户获取短期凭据：

`aws get-role-credentials --account-id {{账户}} --role-name {{角色}} --access-token {{令牌}}`
