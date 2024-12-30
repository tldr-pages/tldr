# btrfs 设备

> 管理 btrfs 文件系统中的设备。
> 更多信息：<https://btrfs.readthedocs.io/en/latest/btrfs-device.html>。

- 向 btrfs 文件系统添加一个或多个设备：

`sudo btrfs device add {{path/to/block_device1}} [{{path/to/block_device2}}] {{path/to/btrfs_filesystem}}`

- 从 btrfs 文件系统中移除一个设备：

`sudo btrfs device remove {{path/to/device|device_id}} [{{...}}]`

- 显示错误统计信息：

`sudo btrfs device stats {{path/to/btrfs_filesystem}}`

- 扫描所有磁盘并通知内核所有检测到的 btrfs 文件系统：

`sudo btrfs device scan --all-devices`

- 显示详细的每个磁盘的分配统计信息：

`sudo btrfs device usage {{path/to/btrfs_filesystem}}`