# flatpak

> 构建、安装和运行 Flatpak 应用和运行时。
> 更多信息：<https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak>.

- 运行已安装应用：

`flatpak run {{应用名}}`

- 从远程源安装应用：

`flatpak install {{远程源名}} {{应用名}}`

- 列出所有应用和运行时：

`flatpak list`

- 更新所有已安装的应用和运行时：

`flatpak update`

- 添加远程源：

`flatpak remote-add --if-not-exists {{远程源名}} {{远程源网址}}`

- 移除一个已安装的应用程序：

`flatpak remove {{应用名}}`

- 显示一个已安装的应用程序的信息：

`flatpak info {{应用名}}`
