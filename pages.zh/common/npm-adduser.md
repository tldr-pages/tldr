# npm adduser

> 添加注册表用户账户。
> 更多信息：<https://docs.npmjs.com/cli/npm-adduser>。

- 在指定的注册表中创建新用户，并将凭证保存到 `.npmrc`：

`npm adduser --registry={{registry_url}}`

- 使用特定作用域登录到私有注册表：

`npm login --scope={{@mycorp}} --registry={{https://registry.mycorp.com}}`

- 从特定作用域注销并移除认证令牌：

`npm logout --scope={{@mycorp}}`

- 在初始化时创建具有特定作用域的包：

`npm init --scope={{@foo}} {{--yes}}`
