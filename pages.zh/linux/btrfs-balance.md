# btrfs balance

> 在 btrfs 文件系统中平衡块组。
> 更多信息：<https://btrfs.readthedocs.io/en/latest/btrfs-balance.html>。

- 显示正在进行或已暂停的平衡操作的状态：

`sudo btrfs balance status {{path/to/btrfs_filesystem}}`

- 平衡所有块组（较慢；重写文件系统中的所有块）：

`sudo btrfs balance start {{path/to/btrfs_filesystem}}`

- 平衡利用率低于 15% 的数据块组，并在后台运行操作：

`sudo btrfs balance start --bg -dusage={{15}} {{path/to/btrfs_filesystem}}`

- 平衡最多 10 个利用率低于 20% 的元数据块，并且在给定设备 `devid` 上至少有 1 个块（参见 `btrfs filesystem show`）：

`sudo btrfs balance start -musage={{20}},limit={{10}},devid={{devid}} {{path/to/btrfs_filesystem}}`

- 将数据块转换为 raid6，元数据块转换为 raid1c3（关于配置文件，请参见 mkfs.btrfs(8)）：

`sudo btrfs balance start -dconvert={{raid6}} -mconvert={{raid1c3}} {{path/to/btrfs_filesystem}}`

- 将数据块转换为 raid1，跳过已转换的块（例如，在之前的转换操作被取消后）：

`sudo btrfs balance start -dconvert={{raid1}},soft {{path/to/btrfs_filesystem}}`

- 取消、暂停或恢复正在进行或已暂停的平衡操作：

`sudo btrfs balance {{cancel|pause|resume}} {{path/to/btrfs_filesystem}}`