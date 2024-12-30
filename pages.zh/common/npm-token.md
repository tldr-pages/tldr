# npm 令牌

> 管理和生成 npm 注册表的身份验证令牌。
> 更多信息：<https://docs.npmjs.com/cli/commands/npm-token>。

- 创建新的身份验证令牌：

`npm token create`

- 列出与帐户关联的所有令牌：

`npm token list`

- 使用令牌 ID 删除特定令牌：

`npm token revoke {{token_id}}`

- 创建只读访问的令牌：

`npm token create --read-only`

- 创建具有发布权限的令牌：

`npm token create --publish`

- 当您登录时，在全局 `.npmrc` 文件中自动配置 npm 令牌：

`npm login`

- 从全局配置中移除令牌：

`npm token revoke {{token_id}}`