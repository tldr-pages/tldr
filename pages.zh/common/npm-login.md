# npm 登录

> 登录到一个注册用户账户。
> 另请参见：`npm logout` 用于注销。
> 更多信息：<https://docs.npmjs.com/cli/commands/npm-login>。

- 登录到一个注册用户账户并将凭据保存到 `.npmrc` 文件中：

`npm login`

- 使用自定义注册表登录：

`npm login --registry={{registry_url}}`

- 使用特定的身份验证策略登录：

`npm login --auth-type={{legacy|web}}`