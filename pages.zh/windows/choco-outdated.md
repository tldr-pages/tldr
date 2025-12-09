# choco outdated

> 使用 Chocolatey 检查过时的包。
> 更多信息：<https://chocolatey.org/docs/commands-outdated>.

- 用表格的形式列出过时的包：

`choco outdated`

- 忽略输出中的固定包：

`choco outdated --ignore-pinned`

- 从自定义的源处检查过时的包：

`choco outdated --source {{源 URL|别名}}`

- 提供一个用户名和密码来进行验证：

`choco outdated --user {{用户名}} --password {{密码}}`
