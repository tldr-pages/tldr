# 垃圾

> 管理垃圾桶/回收站。
> 更多信息：<https://github.com/andreafrancia/trash-cli>。

- 将文件发送到垃圾桶：

`trash {{path/to/file}}`

- 列出垃圾桶中的所有文件：

`trash-list`

- 交互式地从垃圾桶中恢复文件：

`trash-restore`

- 清空垃圾桶：

`trash-empty`

- 永久删除垃圾桶中所有超过10天的文件：

`trash-empty 10`

- 删除垃圾桶中所有匹配特定模式的文件：

`trash-rm "{{*.o}}"`

- 删除所有具有特定原始位置的文件：

`trash-rm {{/path/to/file_or_directory}}`