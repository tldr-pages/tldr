# xbps-remove

> XBPS 工具，用于删除软件包。
> 另见：`xbps`。
> 更多信息：<https://manned.org/xbps-remove.1>。

- 删除一个软件包：

`xbps-remove {{package}}`

- 删除一个软件包及其依赖：

`xbps-remove --recursive {{package}}`

- 删除孤立软件包（作为依赖安装但不再被任何软件包所需）：

`xbps-remove --remove-orphans`

- 从缓存中删除过时的软件包：

`xbps-remove --clean-cache`