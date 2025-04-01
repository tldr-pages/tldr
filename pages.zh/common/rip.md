# rip

> 通过将文件或目录发送到“墓地”来移除它们，允许之后恢复这些文件或目录。
> 更多信息：<https://github.com/nivekuil/rip>.

- 从指定位置移除文件或目录，并将它们放入“墓地”：

`rip {{path/to/file_or_directory}} {{path/to/another/file_or_directory}}`

- 交互式移除文件或目录，在每次移除前提示：

`rip --inspect {{path/to/file_or_directory}} {{path/to/another/file_or_directory}}`

- 列出“墓地”中所有原来位于当前目录的文件和目录：

`rip --seance`

- 永久删除“墓地”中的所有文件和目录：

`rip --decompose`

- 恢复最近一次移除的文件和目录：

`rip --unbury`

- 恢复 `rip --seance` 列出的所有文件和目录：

`rip --seance --unbury`