# nmtui

> 用于控制 NetworkManager 的文本用户界面。
> 使用 `<方向键>` 导航，使用 `<回车>` 选择选项。
> 更多信息： <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmtui.html>.

- 打开用户界面：

`nmtui`

- 列出可用连接，并可选择激活或停用它们：

`nmtui connect`

- 连接到指定网络：

`nmtui connect {{name|uuid|device|SSID}}`

- 编辑、添加或删除指定网络：

`nmtui edit {{name|id}}`

- 设置系统主机名：

`nmtui hostname`