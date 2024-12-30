# choco 升级

> 使用 Chocolatey 升级一个或多个软件包。
> 更多信息：<https://chocolatey.org/docs/commands-upgrade>。

- 升级一个或多个软件包：

`choco upgrade {{package1 package2 ...}}`

- 升级到特定版本的软件包：

`choco upgrade {{package}} --version {{version}}`

- 升级所有软件包：

`choco upgrade all`

- 升级所有软件包，但排除指定的以逗号分隔的软件包：

`choco upgrade all --except "{{package1,package2,...}}"`

- 自动确认所有提示：

`choco upgrade {{package}} --yes`

- 指定一个自定义源以接收软件包：

`choco upgrade {{package}} --source {{source_url|alias}}`

- 提供用户名和密码进行身份验证：

`choco upgrade {{package}} --user {{username}} --password {{password}}`