# btrfs subvolume

> 管理 btrfs 子卷和快照。
> 更多信息：<https://btrfs.readthedocs.io/en/latest/btrfs-subvolume.html>.

- 创建一个新的空子卷：

`sudo btrfs subvolume create {{指向新子卷的路径}}`

- 列出指定文件系统中的所有子卷和快照：

`sudo btrfs subvolume list {{指向 btrfs 文件系统的路径}}`

- 删除一个子卷：

`sudo btrfs subvolume delete {{指向子卷的路径}}`

- 创建现有子卷的只读快照：

`sudo btrfs subvolume snapshot -r {{指向源子卷的路径}} {{指向目标的路径}}`

- 创建现有子卷的读写快照：

`sudo btrfs subvolume snapshot {{指向源子卷的路径}} {{指向目标的路径}}`

- 显示有关子卷的详细信息：

`sudo btrfs subvolume show {{指向子卷的路径}}`
