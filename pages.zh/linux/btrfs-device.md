# btrfs device

> 管理 btrfs 文件系统中的设备。
> 更多信息：<https://btrfs.readthedocs.io/en/latest/btrfs-device.html>.

- 将一个或多个设备添加到 btrfs 文件系统中：

`sudo btrfs device add {{指向设备1的路径}} [{{指向设备2的路径}}] {{指向 btrfs 文件系统的路径}}`

- 从 btrfs 文件系统中删除设备：

`sudo btrfs device remove {{指向设备的路径|设备 ID}} [{{...}}]`

- 显示错误统计：

`sudo btrfs device stats {{指向 btrfs 文件系统的路径}}`

- 扫描所有磁盘并将所有检测到的 btrfs 文件系统通知内核：

`sudo btrfs device scan --all-devices`

- 显示详细的每个磁盘的空间分配统计信息：

`sudo btrfs device usage {{指向 btrfs 文件系统的路径}}`
