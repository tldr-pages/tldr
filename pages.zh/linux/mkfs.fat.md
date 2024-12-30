# mkfs.fat

> 在分区内创建 MS-DOS 文件系统。
> 更多信息：<https://manned.org/mkfs.fat>。

- 在设备 b 的分区 1 上创建 fat 文件系统（`sdb1`）：

`mkfs.fat {{/dev/sdb1}}`

- 创建带有卷标的文件系统：

`mkfs.fat -n {{卷名}} {{/dev/sdb1}}`

- 创建带有卷 ID 的文件系统：

`mkfs.fat -i {{卷_id}} {{/dev/sdb1}}`

- 使用 5 而不是 2 个文件分配表：

`mkfs.fat -f 5 {{/dev/sdb1}}`