# partx

> 解析分区表并通知内核。
> 更多信息：<https://manned.org/partx>。

- 列出块设备或磁盘映像上的分区：

`sudo partx --list {{path/to/device_or_disk_image}}`

- 将指定块设备中找到的所有分区添加到内核：

`sudo partx --add --verbose {{path/to/device_or_disk_image}}`

- 从内核删除找到的所有分区（不更改磁盘上的分区）：

`sudo partx --delete {{path/to/device_or_disk_image}}`