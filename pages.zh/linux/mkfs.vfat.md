# mkfs.vfat

> 在分区内创建一个MS-DOS文件系统。
> 更多信息请访问：<https://manned.org/mkfs.vfat>。

- 在设备b的分区1上创建vfat文件系统（`sdb1`）：

`mkfs.vfat {{/dev/sdb1}}`

- 创建带有卷标的文件系统：

`mkfs.vfat -n {{卷名}} {{/dev/sdb1}}`

- 创建带有卷ID的文件系统：

`mkfs.vfat -i {{卷ID}} {{/dev/sdb1}}`

- 使用5个而不是2个文件分配表：

`mkfs.vfat -f 5 {{/dev/sdb1}}`