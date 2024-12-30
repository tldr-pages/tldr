# pkcon

> PackageKit 控制台程序的命令行客户端，供 Discover 和 Gnome 软件使用，是 'apt' 的替代品。
> 更多信息：<https://manned.org/pkcon>。

- 安装一个软件包：

`pkcon install {{package}}`

- 移除一个软件包：

`pkcon remove {{package}}`

- 刷新软件包缓存：

`pkcon refresh`

- 更新软件包：

`pkcon update`

- 搜索特定的软件包：

`pkcon search {{package}}`

- 列出所有可用的软件包：

`pkcon get-packages`