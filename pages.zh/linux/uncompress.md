# uncompress

> 解压使用 Unix `compress` 命令压缩的文件。
> 更多信息：<https://manned.org/uncompress.1>。

- 解压特定文件：

`uncompress {{path/to/file1.Z path/to/file2.Z ...}}`

- 解压特定文件，同时忽略不存在的文件：

`uncompress -f {{path/to/file1.Z path/to/file2.Z ...}}`

- 写入 `stdout`（不改变任何文件，也不创建 `.Z` 文件）：

`uncompress -c {{path/to/file1.Z path/to/file2.Z ...}}`

- 详细模式（在 `stderr` 中写入关于百分比减少或扩展的信息）：

`uncompress -v {{path/to/file1.Z path/to/file2.Z ...}}`