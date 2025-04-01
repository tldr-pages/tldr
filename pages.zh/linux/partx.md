# partx

> 解析分区表并告知内核。
> 更多信息：<https://manned.org/partx>.

- 列出块设备或磁盘映像上的分区：

`sudo partx {{[-l|--list]}} {{path/to/device_or_disk_image}}`

- 将给定块设备中找到的所有分区添加到内核：

`sudo partx {{[-a|--add]}} {{[-v|--verbose]}} {{path/to/device_or_disk_image}}`

- 从内核中删除所有找到的分区（不会更改磁盘上的分区）：

`sudo partx {{[-d|--delete]}} {{path/to/device_or_disk_image}}`
