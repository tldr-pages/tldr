# uncompress

> 解压使用 Unix `compress` 命令压缩的文件。
> 更多信息：<https://manned.org/uncompress.1>.

- 解压指定的文件：

`uncompress {{path/to/file1.Z path/to/file2.Z ...}}`

- 解压指定的文件，忽略不存在的文件：

`uncompress -f {{path/to/file1.Z path/to/file2.Z ...}}`

- 将输出写入 `stdout`（文件不会被更改，不会创建 `.Z` 文件）：

`uncompress -c {{path/to/file1.Z path/to/file2.Z ...}}`

- 详细模式（在 `stderr` 中显示压缩百分比或扩展信息）：

`uncompress -v {{path/to/file1.Z path/to/file2.Z ...}}`