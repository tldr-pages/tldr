# mkfs.bcachefs

> 在分区中创建一个 `bcachefs` 文件系统。
> 更多信息：<https://bcachefs-docs.readthedocs.io/en/latest/mgmt-formatting.html>.

- 在设备 `X` 上的分区 1 中创建一个 `bcachefs` 文件系统：

`sudo mkfs.bcachefs {{/dev/sdX1}}`

- 创建一个带有卷标签的 `bcachefs` 文件系统：

`sudo mkfs.bcachefs {{[-L|--fs_label]}} {{volume_label}} {{/dev/sdX1}}`