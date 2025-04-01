# sfill

> 安全地覆盖指定目录所在分区的空闲空间和 inode。
> 更多信息：<https://manned.org/sfill>.

- 使用 38 次覆盖来擦除磁盘的空闲空间和 inode（慢但安全）：

`sfill {{/path/to/mounted_disk_directory}}`

- 使用 6 次覆盖来擦除磁盘的空闲空间和 inode（快但安全性较低）并显示状态：

`sfill -l -v {{/path/to/mounted_disk_directory}}`

- 使用 1 次覆盖来擦除磁盘的空闲空间和 inode（非常快但不安全）并显示状态：

`sfill -ll -v {{/path/to/mounted_disk_directory}}`

- 仅覆盖磁盘的空闲空间：

`sfill -I {{/path/to/mounted_disk_directory}}`

- 仅覆盖磁盘的空闲 inode：

`sfill -i {{/path/to/mounted_disk_directory}}`