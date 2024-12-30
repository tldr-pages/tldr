# choco 信息

> 显示有关 Chocolatey 软件包的详细信息。
> 更多信息：<https://chocolatey.org/docs/commands-info>。

- 显示特定软件包的信息：

`choco info {{package}}`

- 仅显示本地软件包的信息：

`choco info {{package}} --local-only`

- 指定自定义源以获取软件包信息：

`choco info {{package}} --source {{source_url|alias}}`

- 提供用户名和密码进行身份验证：

`choco info {{package}} --user {{username}} --password {{password}}`