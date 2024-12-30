# flatpak

> 构建、安装和运行 flatpak 应用程序和运行时。
> 更多信息：<https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak>。

- 运行已安装的应用程序：

`flatpak run {{com.example.app}}`

- 从远程源安装应用程序：

`flatpak install {{remote_name}} {{com.example.app}}`

- 列出已安装的应用程序，忽略运行时：

`flatpak list --app`

- 更新所有已安装的应用程序和运行时：

`flatpak update`

- 添加远程源：

`flatpak remote-add --if-not-exists {{remote_name}} {{remote_url}}`

- 移除已安装的应用程序：

`flatpak remove {{com.example.app}}`

- 移除所有未使用的应用程序：

`flatpak remove --unused`

- 显示已安装应用程序的信息：

`flatpak info {{com.example.app}}`