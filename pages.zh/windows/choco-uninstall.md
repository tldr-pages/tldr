# choco 卸载

> 使用 Chocolatey 卸载软件包。
> 更多信息：<https://chocolatey.org/docs/commands-uninstall>。

- 卸载一个或多个软件包：

`choco 卸载 {{package1 package2 ...}}`

- 卸载特定版本的软件包：

`choco 卸载 {{package}} --version {{version}}`

- 自动确认所有提示：

`choco 卸载 {{package}} --yes`

- 卸载时移除所有依赖项：

`choco 卸载 {{package}} --remove-dependencies`

- 卸载所有软件包：

`choco 卸载 all`