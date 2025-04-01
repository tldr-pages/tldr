# trash

> 管理回收站。
> 更多信息：<https://github.com/andreafrancia/trash-cli>。

- 将文件发送到回收站：

`trash {{path/to/file}}`

- 列出回收站中的所有文件：

`trash-list`

- 交互式地从回收站恢复文件：

`trash-restore`

- 清空回收站：

`trash-empty`

- 永久删除回收站中10天前的文件：

`trash-empty 10`

- 删除回收站中与特定模式匹配的所有文件：

`trash-rm "{{*.o}}"`

- 删除具有特定原始位置的所有文件：

`trash-rm {{/path/to/file_or_directory}}`
