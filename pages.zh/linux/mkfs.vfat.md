# mkfs.vfat

> 在分区内创建一个 MS-DOS 文件系统。
> 更多信息：<https://manned.org/mkfs.vfat>.

- 在设备 b 的分区 1 内创建一个 vfat 文件系统（`sdb1`）：

`mkfs.vfat {{/dev/sdb1}}`

- 创建一个带有卷名的文件系统：

`mkfs.vfat -n {{volume_name}} {{/dev/sdb1}}`

- 创建一个带有卷 ID 的文件系统：

`mkfs.vfat -i {{volume_id}} {{/dev/sdb1}}`

- 使用 5 个而不是 2 个文件分配表：

`mkfs.vfat -f 5 {{/dev/sdb1}}`
