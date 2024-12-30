# zdiff

> 在 `gzip` 压缩档案上调用 `diff`。
> 更多信息：<https://manned.org/zdiff>。

- 比较两个文件，如有必要则解压缩它们：

`zdiff {{path/to/file1.gz}} {{path/to/file2.gz}}`

- 将一个文件与同名的 `gzip` 压缩档案进行比较：

`zdiff {{path/to/file}}`