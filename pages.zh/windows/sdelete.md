# sdelete

> 从磁盘安全地删除文件/目录，或清理卷/物理磁盘上的空闲空间。
> 更多信息请访问：<https://learn.microsoft.com/en-us/sysinternals/downloads/sdelete>。

- 使用 3 次 [p]asses 删除文件：

`sdelete -p 3 {{路径\到\文件1 路径\到\文件2 ...}}`

- 使用 1 次 (默认) 删除文件夹及其 [s]子目录：

`sdelete -s {{路径\到\目录1 路径\到\目录2 ...}}`

- 使用 3 次 [p]asses 清理 D: 卷的空闲空间：

`sdelete -p 3 D:`

- 使用 [z]eros 清理物理磁盘 2 的空闲空间，该磁盘不应包含要清理的任何卷：

`sdelete -z 2`