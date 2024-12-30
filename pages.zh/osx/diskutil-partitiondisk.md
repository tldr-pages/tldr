# diskutil partitionDisk

> 用于管理磁盘和卷内的分区的工具。
> 属于 `diskutil`。
> APM 仅支持 macOS，MBR 为 DOS 优化，而 GPT 兼容大多数现代系统。
> 更多信息：<https://keith.github.io/xcode-man-pages/diskutil.8.html>。

- 使用 APM/MBR/GPT 分区方案重新格式化卷，不留下任何分区（这将擦除卷上的所有数据）：

`diskutil partitionDisk {{/dev/disk_device}} 0 {{APM|MBR|GPT}}`

- 重新格式化卷，然后创建一个使用特定文件系统的单一分区，填满所有空闲空间：

`diskutil partitionDisk {{/dev/disk_device}} 1 {{APM|MBR|GPT}} {{partition_filesystem}} {{partition_name}}`

- 重新格式化卷，然后创建一个使用特定文件系统的单一分区，大小为特定值（例如 `16G` 表示 16GB 或 `50%` 表示填满总卷大小的一半）：

`diskutil partitionDisk {{/dev/disk_device}} 1 {{APM|MBR|GPT}} {{partition_filesystem}} {{partition_name}} {{partition_size}}`

- 重新格式化卷，然后创建多个分区：

`diskutil partitionDisk {{/dev/disk_device}} {{number_of_partitions}} {{APM|MBR|GPT}} {{partition_filesystem1}} {{partition_name1}} {{partition_size1}} {{partition_filesystem2}} {{partition_name2}} {{partition_size2}} ...`

- 列出所有支持的分区文件系统：

`diskutil listFilesystems`