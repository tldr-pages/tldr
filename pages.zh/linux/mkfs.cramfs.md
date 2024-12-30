# mkfs.cramfs

> 在一个分区内创建一个 ROM 文件系统。
> 更多信息：<https://manned.org/mkfs.cramfs>。

- 在设备 b 的分区 1 上创建一个 ROM 文件系统 (`sdb1`)：

`mkfs.cramfs {{/dev/sdb1}}`

- 创建一个带有卷名的 ROM 文件系统：

`mkfs.cramfs -n {{volume_name}} {{/dev/sdb1}}`