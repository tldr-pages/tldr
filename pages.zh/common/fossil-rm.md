# fossil rm

> 从 Fossil 版本控制系统中移除文件或目录。
> 另见：`fossil forget`。
> 更多信息：<https://fossil-scm.org/home/help/rm>。

- 从 Fossil 版本控制系统中移除文件或目录：

`fossil rm {{path/to/file_or_directory}}`

- 从 Fossil 版本控制系统中移除文件或目录，并从磁盘中删除：

`fossil rm --hard {{path/to/file_or_directory}}`

- 将所有先前移除但未提交的文件重新添加到 Fossil 版本控制系统中：

`fossil rm --reset`
