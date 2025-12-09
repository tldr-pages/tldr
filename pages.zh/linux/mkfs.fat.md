# mkfs.fat

> 在分区内创建一个 MS-DOS 文件系统。
> 更多信息：<https://manned.org/mkfs.fat>.

- 在设备 b 的分区 1 内创建一个 FAT 文件系统（`sdb1`）：

`mkfs.fat {{/dev/sdb1}}`

- 创建一个带有卷名的文件系统：

`mkfs.fat -n {{volume_name}} {{/dev/sdb1}}`

- 创建一个带有卷 ID 的文件系统：

`mkfs.fat -i {{volume_id}} {{/dev/sdb1}}`

- 使用 5 个而不是 2 个文件分配表：

`mkfs.fat -f 5 {{/dev/sdb1}}`
