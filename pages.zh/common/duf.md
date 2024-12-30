# duf

> 磁盘使用/空闲实用程序。
> 更多信息：<https://github.com/muesli/duf>。

- 列出可访问的设备：

`duf`

- 列出所有内容（例如伪设备、重复或无法访问的文件系统）：

`duf --all`

- 仅显示指定的设备或挂载点：

`duf {{path/to/directory1 path/to/directory2 ...}}`

- 按指定标准排序输出：

`duf --sort {{size|used|avail|usage}}`

- 显示或隐藏特定文件系统：

`duf --{{only-fs|hide-fs}} {{tmpfs|vfat|ext4|xfs}}`

- 按关键字排序输出：

`duf --sort {{mountpoint|size|used|avail|usage|inodes|inodes_used|inodes_avail|inodes_usage|type|filesystem}}`

- 更改主题（如果 `duf` 无法使用正确的主题）：

`duf --theme {{dark|light}}`