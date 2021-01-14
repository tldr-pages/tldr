# flatpak

> 构建、安装和运行 Flatpak 应用和运行时。

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

- 列出所有已配置的远程源：

`flatpak remote-list`
