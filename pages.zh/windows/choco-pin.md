# choco pin

> 使用 Chocolatey 将一个包固定到指定的版本。
> 被固定版本的包会在更新时自动忽略。
> 更多信息：<https://chocolatey.org/docs/commands-pin>.

- 显示被固定的包以及他们对应的版本号：

`choco pin list`

- 将一个包固定至当前版本：

`choco pin add --name {{包名}}`

- 将一个包固定直指定的版本：

`choco pin add --name {{包名}} --version {{版本号}}`

- 移除指定包的固定状态：

`choco pin remove --name {{包名}}`
