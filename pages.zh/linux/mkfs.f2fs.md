# mkfs.f2fs

> 在分区内创建一个 F2FS 文件系统。
> 更多信息：<https://manned.org/mkfs.f2fs>.

- 在设备 b 的第 1 个分区内创建一个 F2FS 文件系统（`sdb1`）：

`sudo mkfs.f2fs {{/dev/sdb1}}`

- 创建一个带有卷标签的 F2FS 文件系统：

`sudo mkfs.f2fs -l {{volume_label}} {{/dev/sdb1}}`
