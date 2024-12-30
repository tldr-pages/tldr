# npm 添加用户

> 添加一个注册表用户账户。
> 更多信息：<https://docs.npmjs.com/cli/npm-adduser>。

- 在指定的注册表中创建一个新用户并将凭证保存到 `.npmrc`：

`npm adduser --registry={{registry_url}}`

- 使用特定作用域登录到私有注册表：

`npm login --scope={{@mycorp}} --registry={{https://registry.mycorp.com}}`

- 从特定作用域注销并移除身份验证令牌：

`npm logout --scope={{@mycorp}}`

- 在初始化时创建一个作用域包：

`npm init --scope={{@foo}} {{--yes}}`