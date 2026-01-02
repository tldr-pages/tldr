# choco list

> 使用 Chocolatey 显示包列表。
> 更多信息：<https://docs.chocolatey.org/en-us/choco/commands/list/>。

- 列出所有可用的软件包：

`choco list`

- 列出所有本地已安装的软件包：

`choco list --local-only`

- 列出包含本地程序的软件包：

`choco list {{[-i|--include-programs]}}`

- 仅列出已批准的软件包：

`choco list --approved-only`

- 从指定的源列出软件包：

`choco list {{[-s|--source]}} {{源 URL|别名}}`

- 提供用户名和密码进行身份验证：

`choco list --user {{用户名}} --password {{密码}}`
