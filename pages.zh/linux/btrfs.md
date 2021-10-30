# btrfs

> 一种基于写时复制（COW）原理的 Linux 文件系统。
> 此命令也有关于其子命令的文件，例如：`btrfs device`.
> 更多信息：<https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs>.

- 创建子卷：

`sudo btrfs subvolume create {{指向子卷的路径}}`

- 列出子卷：

`sudo btrfs subvolume list {{指向挂载点的路径}}`

- 显示空间使用情况信息：

`sudo btrfs filesystem df {{指向挂载点的路径}}`

- 启用配额（quota）：

`sudo btrfs quota enable {{指向子卷的路径}}`

- 显示配额（quota）：

`sudo btrfs qgroup show {{指向子卷的路径}}`
