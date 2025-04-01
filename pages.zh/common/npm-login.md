# npm login

> 登录到注册表用户帐户。
> 参见：`npm logout` 用于登出。
> 更多信息：<https://docs.npmjs.com/cli/commands/npm-login>。

- 登录到注册表用户帐户，并将凭据保存到 `.npmrc` 文件：

`npm login`

- 使用自定义注册表登录：

`npm login --registry={{registry_url}}`

- 使用特定的认证策略登录：

`npm login --auth-type={{legacy|web}}`
