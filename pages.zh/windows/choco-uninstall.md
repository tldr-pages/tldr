# choco uninstall

> 使用 Chocolatey 卸载一个或多个包。
> 更多信息：<https://chocolatey.org/docs/commands-uninstall>.

- 卸载一个或多个用空格分隔的软件包：

`choco uninstall {{包名 『包名』 ..}}`

- 卸载一个指定版本的包：

`choco uninstall {{包名}} --version {{版本号}}`

- 自动确认所有提示：

`choco uninstall {{包名}} --yes`

- 卸载时同时删除其所有的依赖：

`choco uninstall {{包名}} --remove-dependencies`

- 卸载全部包：

`choco uninstall all`
