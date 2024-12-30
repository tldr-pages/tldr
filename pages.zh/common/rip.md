# rip

> 通过将文件或目录发送到墓地来删除它们，从而允许恢复。
> 更多信息：<https://github.com/nivekuil/rip>。

- 从指定位置删除文件或目录并将其放入墓地：

`rip {{path/to/file_or_directory}} {{path/to/another/file_or_directory}}`

- 交互式删除文件或目录，在每次删除之前进行提示：

`rip --inspect {{path/to/file_or_directory}} {{path/to/another/file_or_directory}}`

- 列出当前目录中最初存在的墓地中的所有文件和目录：

`rip --seance`

- 永久删除墓地中的每个文件和目录：

`rip --decompose`

- 恢复最近删除的文件和目录：

`rip --unbury`

- 恢复`rip --seance`列出的每个文件和目录：

`rip --seance --unbury`