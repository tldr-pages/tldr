# sdelete

> 安全地从磁盘中删除文件/目录，或清理卷/物理磁盘上的空闲空间。
> 更多信息：<https://learn.microsoft.com/en-us/sysinternals/downloads/sdelete>.

- 以 3 次 [p]ass（遍历）删除文件：

`sdelete -p 3 {{path\to\file1 path\to\file2 ...}}`

- 以 1 次 [s]ubdirectories pass（遍历子目录，这是默认设置）删除文件夹及其子目录：

`sdelete -s {{path\to\directory1 path\to\directory2 ...}}`

- 以 3 次 [p]ass（遍历）清理卷 D: 的空闲空间：

`sdelete -p 3 D:`

- 以 [z]eros（零）清理物理磁盘 2 的空闲空间，该磁盘不应包含任何需要清理的卷：

`sdelete -z 2`
