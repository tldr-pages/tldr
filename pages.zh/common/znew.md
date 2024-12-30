# znew

> 将 `.Z` 格式的文件重新压缩为 gzip 格式。
> 更多信息请访问: <https://manned.org/znew>。

- 将 `.Z` 格式的文件重新压缩为 gzip 格式：

`znew {{path/to/file1.Z}}`

- 重新压缩多个文件并显示每个文件的大小减少百分比：

`znew -v {{path/to/file1.Z path/to/file2.Z ...}}`

- 使用最慢的压缩方法重新压缩文件（以获得最佳压缩效果）：

`znew -9 {{path/to/file1.Z}}`

- 重新压缩文件，如果 `.Z` 文件小于 gzip 文件，则[K]eep `.Z` 文件：

`znew -K {{path/to/file1.Z}}`