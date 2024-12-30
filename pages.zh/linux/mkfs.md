# mkfs

> 在硬盘分区上构建一个Linux文件系统。
> 此命令已被弃用，建议使用特定文件系统的mkfs.<type>工具。
> 更多信息：<https://manned.org/mkfs>。

- 在分区上构建一个Linux ext2文件系统：

`mkfs {{path/to/partition}}`

- 构建指定类型的文件系统：

`mkfs -t {{ext4}} {{path/to/partition}}`

- 构建指定类型的文件系统并检查坏块：

`mkfs -c -t {{ntfs}} {{path/to/partition}}`