# mkfs.exfat

> 在分区内创建exfat文件系统。
> 更多信息：<https://manned.org/mkfs.exfat>。

- 在设备b的分区1上创建exfat文件系统（`sdb1`）：

`mkfs.exfat {{/dev/sdb1}}`

- 创建带有卷标的文件系统：

`mkfs.exfat -n {{卷标名称}} {{/dev/sdb1}}`

- 创建带有卷ID的文件系统：

`mkfs.exfat -i {{卷ID}} {{/dev/sdb1}}`