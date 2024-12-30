# tmutil

> 用于管理 Time Machine 备份的工具。大多数操作需要 root 权限。
> 更多信息：<https://keith.github.io/xcode-man-pages/tmutil.8.html>。

- 将 HFS+ 驱动器设置为备份目标：

`sudo tmutil setdestination {{path/to/disk_mount_point}}`

- 将 APF 共享或 SMB 共享设置为备份目标：

`sudo tmutil setdestination "{{protocol://user[:password]@host/share}}"`

- 将给定目标追加到目标列表中：

`sudo tmutil setdestination -a {{destination}}`

- 启用自动备份：

`sudo tmutil enable`

- 禁用自动备份：

`sudo tmutil disable`

- 如果没有正在运行的备份，则启动备份，并释放对终端的控制：

`sudo tmutil startbackup`

- 启动备份并阻塞直到备份完成：

`sudo tmutil startbackup -b`

- 停止备份：

`sudo tmutil stopbackup`