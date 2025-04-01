# choco info

> 显示有关 Chocolatey 包的详细信息。
> 更多信息：<https://chocolatey.org/docs/commands-info>.

- 显示指定包的信息：

`choco info {{包名}}`

- 显示一个本地已安装包的信息：

`choco info {{包名}} --local-only`

- 从一个自定义的源来获取包的信息：

`choco info {{包名}} --source {{源 URL|别名}}`

- 提供一个用户名和密码来进行验证：

`choco info {{包名}} --user {{用户名}} --password {{密码}}`
