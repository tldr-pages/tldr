# choco list

> 使用 Chocolatey 显示包列表。
> 更多信息：<https://chocolatey.org/docs/commands-list>.

- 列出所有可用的包：

`choco list`

- 列出所有本地已安装的包：

`choco list --local-only`

- 显示包含本地程序的列表：

`choco list --include-programs`

- 只显示已批准的包：

`choco list --approved-only`

- Specify a custom source to display packages from 指定一个源来显示包列表：

`choco list --source {{源 URL|别名}}`

- 提供一个用户名和密码来进行验证：

`choco list --user {{用户名}} --password {{密码}}`
