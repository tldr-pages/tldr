# fossil rm

> 从Fossil版本控制中移除文件或目录。
> 另见: `fossil forget`。
> 更多信息: <https://fossil-scm.org/home/help/rm>。

- 从Fossil版本控制中移除文件或目录：

`fossil rm {{path/to/file_or_directory}}`

- 从Fossil版本控制中移除文件或目录，并从磁盘中删除它：

`fossil rm --hard {{path/to/file_or_directory}}`

- 重新添加所有之前移除且未提交的文件到Fossil版本控制：

`fossil rm --reset`