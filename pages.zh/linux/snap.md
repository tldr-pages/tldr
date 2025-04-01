# snap

> 管理“snap”自包含软件包。
> 类似于 `.deb` 包的 `apt`。
> 更多信息：<https://manned.org/snap>。

- 搜索软件包：

`snap find {{query}}`

- 安装软件包：

`snap install {{package}}`

- 更新软件包：

`snap refresh {{package}}`

- 将软件包更新到另一个通道（轨道、风险或分支）：

`snap refresh {{package}} --channel={{channel}}`

- 更新所有软件包：

`snap refresh`

- 显示已安装 snap 软件的基本信息：

`snap list`

- 卸载软件包：

`snap remove {{package}}`

- 检查系统中最近的 snap 变更：

`snap changes`
