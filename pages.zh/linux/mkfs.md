# mkfs

> 在硬盘分区上建立一个Linux文件系统。
> 该命令已被废弃，建议使用特定文件系统的 mkfs.<type> 工具。
> 更多信息： <https://manned.org/mkfs>.

- 在分区上建立一个Linux ext2文件系统：

`mkfs {{path/to/partition}}`

- 建立指定类型的文件系统：

`mkfs -t {{ext4}} {{path/to/partition}}`

- 建立指定类型的文件系统并检查坏块：

`mkfs -c -t {{ntfs}} {{path/to/partition}}`
