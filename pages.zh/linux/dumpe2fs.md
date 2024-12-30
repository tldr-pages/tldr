# dumpe2fs

> 打印 ext2/ext3/ext4 文件系统的超级块和块组信息。
> 在运行此命令之前，请使用 `umount {{设备}}` 卸载分区。
> 更多信息：<https://manned.org/dumpe2fs>。

- 显示 ext2、ext3 和 ext4 文件系统信息：

`dumpe2fs {{/dev/sdXN}}`

- 显示文件系统中保留为坏块的块：

`dumpe2fs -b {{/dev/sdXN}}`

- 强制显示文件系统信息，即使有无法识别的特征标志：

`dumpe2fs -f {{/dev/sdXN}}`

- 仅显示超级块信息，而不显示任何块组描述符详细信息：

`dumpe2fs -h {{/dev/sdXN}}`

- 以十六进制格式打印详细的组信息块编号：

`dumpe2fs -x {{/dev/sdXN}}`