# btrfs

> 一个基于写时复制（COW）原理的 Linux 文件系统。
> 一些子命令，例如 `device`，具有自己的使用文档。
> 更多信息：<https://btrfs.readthedocs.io/en/latest/btrfs.html>。

- 创建子卷：

`sudo btrfs subvolume create {{path/to/subvolume}}`

- 列出子卷：

`sudo btrfs subvolume list {{path/to/mount_point}}`

- 显示空间使用信息：

`sudo btrfs filesystem df {{path/to/mount_point}}`

- 启用配额：

`sudo btrfs quota enable {{path/to/subvolume}}`

- 显示配额：

`sudo btrfs qgroup show {{path/to/subvolume}}`