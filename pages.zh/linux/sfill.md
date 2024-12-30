# sfill

> 安全地覆盖指定目录所在分区的空闲空间和inode。
> 更多信息：<https://manned.org/sfill>。

- 使用38次写入覆盖磁盘的空闲空间和inode（慢但安全）：

`sfill {{/path/to/mounted_disk_directory}}`

- 使用6次写入覆盖磁盘的空闲空间和inode（快速但不太安全）并显示状态：

`sfill -l -v {{/path/to/mounted_disk_directory}}`

- 使用1次写入覆盖磁盘的空闲空间和inode（非常快速但不安全）并显示状态：

`sfill -ll -v {{/path/to/mounted_disk_directory}}`

- 仅覆盖磁盘的空闲空间：

`sfill -I {{/path/to/mounted_disk_directory}}`

- 仅覆盖磁盘的空闲inode：

`sfill -i {{/path/to/mounted_disk_directory}}`