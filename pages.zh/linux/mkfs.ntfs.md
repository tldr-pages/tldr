# mkfs.ntfs

> 在分区内创建 NTFS 文件系统。
> 更多信息：<https://manned.org/mkfs.ntfs>。

- 在设备 b 的分区 1 上创建 NTFS 文件系统（`sdb1`）：

`mkfs.ntfs {{/dev/sdb1}}`

- 创建带有卷标的文件系统：

`mkfs.ntfs -L {{volume_label}} {{/dev/sdb1}}`

- 创建具有特定 UUID 的文件系统：

`mkfs.ntfs -U {{UUID}} {{/dev/sdb1}}`