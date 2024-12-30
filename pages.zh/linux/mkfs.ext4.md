# mkfs.ext4

> 在一个分区内创建 ext4 文件系统。
> 更多信息：<https://manned.org/mkfs.ext4>。

- 在设备 b 的分区 1 上创建 ext4 文件系统（`sdb1`）：

`sudo mkfs.ext4 {{/dev/sdb1}}`

- 创建一个带有卷标的 ext4 文件系统：

`sudo mkfs.ext4 -L {{volume_label}} {{/dev/sdb1}}`