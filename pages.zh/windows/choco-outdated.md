# choco 过期

> 使用 Chocolatey 检查过期的软件包。
> 更多信息：<https://chocolatey.org/docs/commands-outdated>。

- 以表格格式显示过期软件包的列表：

`choco outdated`

- 在输出中忽略已固定的软件包：

`choco outdated --ignore-pinned`

- 指定自定义源以检查软件包：

`choco outdated --source {{source_url|alias}}`

- 提供用户名和密码进行身份验证：

`choco outdated --user {{username}} --password {{password}}`