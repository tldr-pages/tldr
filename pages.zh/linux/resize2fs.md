# resize2fs

> 调整 ext2、ext3 或 ext4 文件系统的大小。
> 不会调整底层分区的大小。可能需要先卸载文件系统，更多详细信息请参阅手册页。
> 更多信息：<https://manned.org/resize2fs>。

- 自动调整文件系统大小：

`resize2fs {{/dev/sdXN}}`

- 将文件系统调整为 40G 的大小，并显示进度条：

`resize2fs -p {{/dev/sdXN}} {{40G}}`

- 将文件系统缩小到其最小可能大小：

`resize2fs -M {{/dev/sdXN}}`