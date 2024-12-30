# btrfs 清理

> 清理 btrfs 文件系统以验证数据完整性。
> 建议每月运行一次清理。
> 更多信息：<https://btrfs.readthedocs.io/en/latest/btrfs-scrub.html>。

- 开始清理：

`sudo btrfs scrub start {{path/to/btrfs_mount}}`

- 显示正在进行或上次完成的清理状态：

`sudo btrfs scrub status {{path/to/btrfs_mount}}`

- 取消正在进行的清理：

`sudo btrfs scrub cancel {{path/to/btrfs_mount}}`

- 恢复之前取消的清理：

`sudo btrfs scrub resume {{path/to/btrfs_mount}}`

- 开始清理，但在清理完成之前等待退出：

`sudo btrfs scrub start -B {{path/to/btrfs_mount}}`

- 以静默模式开始清理（不打印错误或统计信息）：

`sudo btrfs scrub start -q {{path/to/btrfs_mount}}`