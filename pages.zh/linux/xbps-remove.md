# xbps-remove

> XBPS 工具用于移除软件包。
> 参见：`xbps`。
> 更多信息：<https://manned.org/xbps-remove.1>.

- 移除一个软件包：

`xbps-remove {{package}}`

- 移除一个软件包及其依赖：

`xbps-remove --recursive {{package}}`

- 移除孤立的软件包（作为依赖安装但已不再被任何软件包需要）：

`xbps-remove --remove-orphans`

- 从缓存中移除过时的软件包：

`xbps-remove --clean-cache`
