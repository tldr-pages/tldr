# btrfs 平衡

> 在 btrfs 文件系统上平衡块组。
> 更多信息：<https://btrfs.readthedocs.io/en/latest/btrfs-balance.html>。

- 显示正在运行或已暂停的平衡操作的状态：

`sudo btrfs balance status {{path/to/btrfs_filesystem}}`

- 平衡所有块组（慢；重新写入文件系统中的所有块）：

`sudo btrfs balance start {{path/to/btrfs_filesystem}}`

- 在后台平衡使用率少于 15% 的数据块组：

`sudo btrfs balance start --bg -dusage={{15}} {{path/to/btrfs_filesystem}}`

- 平衡最大 10 个使用率少于 20% 且在给定设备 `devid` 上至少有 1 个块的元数据块（参见 `btrfs filesystem show`）：

`sudo btrfs balance start -musage={{20}},limit={{10}},devid={{devid}} {{path/to/btrfs_filesystem}}`

- 将数据块转换为 raid6，将元数据转换为 raid1c3（请参见 mkfs.btrfs(8) 了解配置文件）：

`sudo btrfs balance start -dconvert={{raid6}} -mconvert={{raid1c3}} {{path/to/btrfs_filesystem}}`

- 将数据块转换为 raid1，跳过已转换的块（例如，在先前取消的转换操作后）：

`sudo btrfs balance start -dconvert={{raid1}},soft {{path/to/btrfs_filesystem}}`

- 取消、暂停或恢复正在运行或已暂停的平衡操作：

`sudo btrfs balance {{cancel|pause|resume}} {{path/to/btrfs_filesystem}}`