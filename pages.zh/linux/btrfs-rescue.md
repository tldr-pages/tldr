# btrfs rescue

> 尝试恢复受损的 btrfs 文件系统。
> 更多信息：<https://btrfs.readthedocs.io/en/latest/btrfs-rescue.html>.

- 重建文件系统元数据树（非常慢）：

`sudo btrfs rescue chunk-recover {{path/to/partition}}`

- 修复与设备大小对齐相关的问题（例如，超级块总字节不匹配无法挂载文件系统）：

`sudo btrfs rescue fix-device-size {{path/to/partition}}`

- 从正确的副本中恢复损坏的超级块（恢复文件系统树的根）：

`sudo btrfs rescue super-recover {{path/to/partition}}`

- 从中断的事务中恢复（修复日志重放问题）：

`sudo btrfs rescue zero-log {{path/to/partition}}`

- 当 `mknod` 未安装时，创建 `/dev/btrfs-control` 控制设备：

`sudo btrfs rescue create-control-device`
