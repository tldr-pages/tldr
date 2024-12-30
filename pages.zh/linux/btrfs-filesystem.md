# btrfs 文件系统

> 管理 btrfs 文件系统。
> 更多信息：<https://btrfs.readthedocs.io/en/latest/btrfs-filesystem.html>。

- 显示文件系统使用情况（可选择以 root 身份运行以显示详细信息）：

`btrfs filesystem usage {{path/to/btrfs_mount}}`

- 按单个设备显示使用情况：

`sudo btrfs filesystem show {{path/to/btrfs_mount}}`

- 在 btrfs 文件系统上对单个文件进行碎片整理（在去重代理运行时避免此操作）：

`sudo btrfs filesystem defragment -v {{path/to/file}}`

- 递归地对目录进行碎片整理（不跨越子卷边界）：

`sudo btrfs filesystem defragment -v -r {{path/to/directory}}`

- 强制将未写入的数据块同步到磁盘：

`sudo btrfs filesystem sync {{path/to/btrfs_mount}}`

- 递归总结目录中文件的磁盘使用情况：

`sudo btrfs filesystem du --summarize {{path/to/directory}}`