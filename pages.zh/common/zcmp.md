# zcmp

> 比较压缩文件。
> 更多信息：<https://manned.org/zcmp>。

- 在两个通过 `gzip` 压缩的文件上调用 `cmp`：

`zcmp {{path/to/file1.gz}} {{path/to/file2.gz}}`

- 将一个文件与其 gzipped 版本进行比较（假设 `.gz` 文件已存在）：

`zcmp {{path/to/file}}`