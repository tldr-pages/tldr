# zipnote

> 查看、添加或编辑 Zip 压缩档案的评论。
> 也可以在 Zip 压缩档案中重命名文件。
> 更多信息：<https://manned.org/zipnote>。

- 查看 Zip 压缩档案的评论：

`zipnote {{path/to/file.zip}}`

- 将 Zip 压缩档案的评论提取到文件中：

`zipnote {{path/to/file.zip}} > {{path/to/file.txt}}`

- 从文件中添加/更新 Zip 压缩档案的评论：

`zipnote -w {{path/to/file.zip}} < {{path/to/file.txt}}`