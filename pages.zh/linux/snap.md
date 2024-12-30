# snap

> 管理 "snap" 自包含软件包。
> 类似于 `apt` 对于 `.deb` 的作用。
> 更多信息：<https://manned.org/snap>。

- 搜索一个软件包：

`snap find {{query}}`

- 安装一个软件包：

`snap install {{package}}`

- 更新一个软件包：

`snap refresh {{package}}`

- 将一个软件包更新到另一个通道（轨道、风险或分支）：

`snap refresh {{package}} --channel={{channel}}`

- 更新所有软件包：

`snap refresh`

- 显示已安装的 snap 软件的基本信息：

`snap list`

- 卸载一个软件包：

`snap remove {{package}}`

- 检查系统中的最近 snap 更改：

`snap changes`