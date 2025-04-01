# diskutil partitionDisk

> 用于管理磁盘和卷内的分区。
> 属于 `diskutil` 工具。
> APM 仅支持 macOS，MBR 优化用于 DOS，而 GPT 适用于大多数现代系统。
> 更多信息：<https://keith.github.io/xcode-man-pages/diskutil.8.html>.

- 使用 APM/MBR/GPT 分区方案重新格式化卷，不留任何分区（这将擦除卷上的所有数据）：

`diskutil partitionDisk {{/dev/disk_device}} 0 {{APM|MBR|GPT}}`

- 重新格式化卷，然后创建一个使用特定文件系统的分区，并填充所有可用空间：

`diskutil partitionDisk {{/dev/disk_device}} 1 {{APM|MBR|GPT}} {{partition_filesystem}} {{partition_name}}`

- 重新格式化卷，然后创建一个使用特定文件系统并指定大小（例如 `16G` 表示 16GB 或 `50%` 表示占据总卷大小的一半）的分区：

`diskutil partitionDisk {{/dev/disk_device}} 1 {{APM|MBR|GPT}} {{partition_filesystem}} {{partition_name}} {{partition_size}}`

- 重新格式化卷，然后创建多个分区：

`diskutil partitionDisk {{/dev/disk_device}} {{number_of_partitions}} {{APM|MBR|GPT}} {{partition_filesystem1}} {{partition_name1}} {{partition_size1}} {{partition_filesystem2}} {{partition_name2}} {{partition_size2}} ...`

- 列出所有支持的分区文件系统：

`diskutil listFilesystems`