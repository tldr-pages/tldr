# mkfs.exfat

> 在分区内创建一个 exFAT 文件系统。
> 更多信息：<https://manned.org/mkfs.exfat>。

- 在设备 b 的分区 1 内创建一个 exFAT 文件系统（`sdb1`）：

`sudo mkfs.exfat {{/dev/sdb1}}`

- 创建一个带有卷名的文件系统：

`sudo mkfs.exfat {{[-L|--volume-label]}} {{volume_name}} {{/dev/sdXY}}`

- 创建一个带有卷 ID 的文件系统：

`sudo mkfs.exfat {{[-U|--volume-guid]}} {{volume_id}} {{/dev/sdXY}}`
