# choco pin

> 使用 Chocolatey 将软件包固定在某个版本。
> 固定的软件包在升级时会自动被跳过。
> 更多信息：<https://chocolatey.org/docs/commands-pin>。

- 显示固定软件包及其版本的列表：

`choco pin list`

- 将软件包固定在其当前版本：

`choco pin add --name {{package}}`

- 将软件包固定在特定版本：

`choco pin add --name {{package}} --version {{version}}`

- 移除特定软件包的固定：

`choco pin remove --name {{package}}`