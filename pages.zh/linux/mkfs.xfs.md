# mkfs.xfs

> 在分区中创建一个XFS文件系统。
> 更多信息：<https://manned.org/mkfs.xfs>。

- 在设备（`X`）的分区1中创建一个XFS文件系统：

`sudo mkfs.xfs {{/dev/sdX1}}`

- 使用卷标创建一个XFS文件系统：

`sudo mkfs.xfs -L {{volume_label}} {{/dev/sdX1}}`