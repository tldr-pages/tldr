# trash

> 管理回收站。
> 更多信息：<https://github.com/andreafrancia/trash-cli>。

- 将文件移入回收站：

`trash {{路径/到/文件}}`

- 列出回收站中的所有文件：

`trash-list`

- 以交互方式从回收站恢复文件：

`trash-restore`

- 清空回收站：

`trash-empty`

- 永久删除回收站中超过 10 天的所有文件：

`trash-empty 10`

- 删除回收站中匹配指定 glob 模式的所有文件：

`trash-rm "{{*.o}}"`

- 删除具有指定原始位置的所有文件：

`trash-rm /{{路径/到/文件或目录}}`
