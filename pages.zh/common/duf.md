# duf

> 磁盘占用/空闲实用工具。
> 更多信息：<https://github.com/muesli/duf>.

- 列出可访问设备：

`duf`

- 列出所有（如伪文件系统，重复文件系统或不可访问的文件系统）：

`duf --all`

- 只显示指定的设备或挂载点：

`duf {{路径/到/文件夹1 路径/到/文件夹2 ...}}`

- 根据指定条件排序输出：

`duf --sort {{size|used|avail|usage}}`

- 显示或隐藏指定文件系统：

`duf --{{only-fs|hide-fs}} {{tmpfs|vfat|ext4|xfs}}`

- 根据键排序输出：

`duf --sort {{mountpoint|size|used|avail|usage|inodes|inodes_used|inodes_avail|inodes_usage|type|filesystem}}`

- 更改主题（如果 `duf` 未能使用正确的主题）：

`duf --theme {{dark|light}}`
