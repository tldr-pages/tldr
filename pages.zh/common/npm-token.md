# npm token

> 管理和生成 npm 注册表的认证令牌。
> 更多信息：<https://docs.npmjs.com/cli/commands/npm-token>.

- 创建一个新的认证令牌：

`npm token create`

- 列出与账户关联的所有令牌：

`npm token list`

- 使用令牌 ID 删除特定的令牌：

`npm token revoke {{token_id}}`

- 创建一个只读访问的令牌：

`npm token create --read-only`

- 创建一个带有发布权限的令牌：

`npm token create --publish`

- 在登录时自动在全局 `.npmrc` 文件中配置 npm 令牌：

`npm login`

- 从全局配置中移除一个令牌：

`npm token revoke {{token_id}}`
