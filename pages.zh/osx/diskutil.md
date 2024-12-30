# diskutil

> 用于管理本地磁盘和卷的实用工具。
> 一些子命令例如 `partitiondisk` 有自己的使用文档。
> 更多信息：<https://keith.github.io/xcode-man-pages/diskutil.8.html>。

- 列出所有当前可用的磁盘、分区和已挂载的卷：

`diskutil list`

- 修复卷的文件系统数据结构：

`diskutil repairVolume {{/dev/disk_device}}`

- 卸载一个卷：

`diskutil unmountDisk {{/dev/disk_device}}`

- 弹出 CD/DVD（先卸载）：

`diskutil eject {{/dev/disk_device1}}`