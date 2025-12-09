# df

> 显示文件系统磁盘空间使用情况的概览。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/df-invocation.html>.

- 显示磁盘使用情况：

`df`

- 以可读的形式显示磁盘使用情况：

`df {{[-h|--human-readable]}}`

- 显示给定文件或目录的磁盘使用情况：

`df {{路径/到/文件或目录}}`

- 包括空闲 inode 数量的统计信息：

`df {{[-i|--inodes]}}`

- 显示文件系统但排除指定的类型：

`df {{[-x|--exclude-type]}} {{squashfs}} {{[-x|--exclude-type]}} {{tmpfs}}`

- 显示文件系统类型：

`df {{[-T|--print-type]}}`
