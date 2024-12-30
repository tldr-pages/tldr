# df

> 显示文件系统磁盘空间使用情况的概述。
> 更多信息：<https://www.gnu.org/software/coreutils/df>。

- 显示所有文件系统及其磁盘使用情况：

`df`

- 以人类可读的形式显示所有文件系统及其磁盘使用情况：

`df {{-h|--human-readable}}`

- 显示包含给定文件或目录的文件系统及其磁盘使用情况：

`df {{path/to/file_or_directory}}`

- 包括空闲inode的统计信息：

`df {{-i|--inodes}}`

- 显示文件系统，但排除指定的类型：

`df {{-x|--exclude-type}} {{squashfs}} {{-x|--exclude-type}} {{tmpfs}}`

- 显示文件系统类型：

`df {{-T|--print-type}}`