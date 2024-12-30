# btrfs 子卷

> 管理 btrfs 子卷和快照。
> 更多信息：<https://btrfs.readthedocs.io/en/latest/btrfs-subvolume.html>。

- 创建一个新的空子卷：

`sudo btrfs subvolume create {{path/to/new_subvolume}}`

- 列出指定文件系统中的所有子卷和快照：

`sudo btrfs subvolume list {{path/to/btrfs_filesystem}}`

- 删除一个子卷：

`sudo btrfs subvolume delete {{path/to/subvolume}}`

- 创建一个现有子卷的只读快照：

`sudo btrfs subvolume snapshot -r {{path/to/source_subvolume}} {{path/to/target}}`

- 创建一个现有子卷的读写快照：

`sudo btrfs subvolume snapshot {{path/to/source_subvolume}} {{path/to/target}}`

- 显示有关子卷的详细信息：

`sudo btrfs subvolume show {{path/to/subvolume}}`