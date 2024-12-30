# choco 列表

> 显示 Chocolatey 的软件包列表。
> 更多信息：<https://chocolatey.org/docs/commands-list>。

- 显示所有可用的软件包：

`choco list`

- 显示所有本地安装的软件包：

`choco list --local-only`

- 显示包括本地程序在内的列表：

`choco list --include-programs`

- 仅显示已批准的软件包：

`choco list --approved-only`

- 指定自定义源以显示软件包：

`choco list --source {{source_url|alias}}`

- 提供用户名和密码进行身份验证：

`choco list --user {{username}} --password {{password}}`