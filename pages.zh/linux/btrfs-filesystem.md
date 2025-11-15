# btrfs filesystem

> 管理 btrfs 文件系统。
> 更多信息：<https://btrfs.readthedocs.io/en/latest/btrfs-filesystem.html>.

- 显示文件系统使用情况（可以选择以 root 身份运行以显示详细信息）：

`btrfs filesystem usage {{指向挂载点的路径}}`

- 显示各个设备的使用情况：

`sudo btrfs filesystem show {{指向挂载点的路径}}`

- 对 btrfs 文件系统上的单个文件进行碎片整理（避免在运行数据去重的同时运行）：

`sudo btrfs filesystem defragment -v {{指向文件的路径}}`

- 递归对目录进行碎片整理（不跨越子卷边界）：

`sudo btrfs filesystem defragment -v -r {{指向目录的路径}}`

- 强制将未写入的数据块同步到磁盘：

`sudo btrfs filesystem sync {{指向挂载点的路径}}`

- 递归总结目录中文件的磁盘使用情况：

`sudo btrfs filesystem du --summarize {{指向目录的路径}}`
