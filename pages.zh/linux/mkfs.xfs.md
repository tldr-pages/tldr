# mkfs.xfs

> 在分区中创建 XFS 文件系统。
> 更多信息：<https://manned.org/mkfs.xfs>.

- 在设备 `X` 的分区 1 中创建 XFS 文件系统：

`sudo mkfs.xfs {{/dev/sdX1}}`

- 创建带有卷标名称的 XFS 文件系统：

`sudo mkfs.xfs -L {{volume_label}} {{/dev/sdX1}}`