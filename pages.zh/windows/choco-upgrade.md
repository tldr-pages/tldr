# choco upgrade

> 使用 Chocolatey 升级一个或多个包。
> 更多信息：<https://chocolatey.org/docs/commands-upgrade>.

- 升级一个或多个用空格分隔的软件包：

`choco upgrade {{包名 包名 ..}}`

- 将一个包升级到指定版本：

`choco upgrade {{包名}} --version {{版本号}}`

- 升级全部包：

`choco upgrade all`

- 升级除指定的用逗号分隔的包之外的所有包：

`choco upgrade all --except "{{包名 , 包名 ..}}"`

- 自动确认所有提示：

`choco upgrade {{包名}} --yes`

- 从自定义源处升级包：

`choco upgrade {{包名}} --source {{源 URL|别名}}`

- 提供一个用户名和密码来进行验证：

`choco upgrade {{包}} --user {{用户名}} --password {{密码}}`
