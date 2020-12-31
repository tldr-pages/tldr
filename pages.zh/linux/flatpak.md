# flatpak

> 构建、安装和运行 Flatpak 应用和运行时。

- 运行已安装应用：

`flatpak run {{name}}`

- 从远程源安装应用：

`flatpak install {{remote}} {{name}}`

- 列出所有应用和运行时：

`flatpak list`

- 更新所有已安装的应用和运行时：

`flatpak update`

- 添加远程源：

`flatpak remote-add --if-not-exists {{remote_name}} {{remote_url}}`

- 列出所有已配置的远程源：

`flatpak remote-list`
