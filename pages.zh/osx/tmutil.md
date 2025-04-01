# tmutil

> 管理 Time Machine 备份的工具。大多数操作动词需要 root 权限。
> 更多信息：<https://keith.github.io/xcode-man-pages/tmutil.8.html>.

- 将 HFS+ 磁盘设置为备份目标：

`sudo tmutil setdestination {{path/to/disk_mount_point}}`

- 将 APFS 共享或 SMB 共享设置为备份目标：

`sudo tmutil setdestination "{{protocol://user[:password]@host/share}}"`

- 将给定的目标添加到目标列表中：

`sudo tmutil setdestination -a {{destination}}`

- 启用自动备份：

`sudo tmutil enable`

- 禁用自动备份：

`sudo tmutil disable`

- 如果没有备份正在运行，则开始一个备份，并释放对 shell 的控制：

`sudo tmutil startbackup`

- 开始一个备份并阻塞，直到备份完成：

`sudo tmutil startbackup -b`

- 停止一个备份：

`sudo tmutil stopbackup`