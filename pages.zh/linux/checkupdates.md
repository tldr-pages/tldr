# checkupdates

> 检查 Arch Linux 中待处理的更新。
> 更多信息：<https://manned.org/checkupdates.8>。

- 列出待处理的更新：

`checkupdates`

- 列出待处理的更新并将软件包下载到 `pacman` 缓存：

`checkupdates --download`

- 使用特定的 `pacman` 数据库列出待处理的更新：

`CHECKUPDATES_DB={{path/to/directory}} checkupdates`

- 显示帮助信息：

`checkupdates --help`