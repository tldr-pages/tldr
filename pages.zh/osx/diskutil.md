# diskutil

> 用于管理本地磁盘和卷的实用程序。
> 更多信息：<https://keith.github.io/xcode-man-pages/diskutil.8.html>.

- 列出所有当前可用的磁盘、分区和已装入的卷：

`diskutil list`

- 修复卷的文件系统数据结构：

`diskutil repairVolume {{目标卷文件}}`

- 卸载卷：

`diskutil unmountDisk {{目标卷文件}}`

- 弹出 CD/DVD（先卸载）：

`diskutil eject {{/dev/ 光驱文件名}}`
