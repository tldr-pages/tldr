# nmtui

> 控制 NetworkManager 的文本用户界面。
> 使用箭头键导航，按 Enter 选择选项。
> 更多信息：<https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmtui.html>。

- 打开用户界面：

`nmtui`

- 列出可用的连接，并可以选择激活或停用它们：

`nmtui connect`

- 连接到指定的网络：

`nmtui connect {{name|uuid|device|SSID}}`

- 编辑/添加/删除指定的网络：

`nmtui edit {{name|id}}`

- 设置系统主机名：

`nmtui hostname`