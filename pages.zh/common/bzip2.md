# bzip2

> 一种块排序文件压缩工具。
> 更多信息：<https://manned.org/bzip2>。

- 压缩文件：

`bzip2 {{path/to/file_to_compress}}`

- [d]解压文件：

`bzip2 -d {{path/to/compressed_file.bz2}}`

- [d]解压文件到 `stdout`：

`bzip2 -dc {{path/to/compressed_file.bz2}}`

- 测试归档文件内每个文件的完整性：

`bzip2 --test {{path/to/compressed_file.bz2}}`

- 显示处理过的每个文件的压缩比及详细信息：

`bzip2 --verbose {{path/to/compressed_files.bz2}}`

- 解压文件并覆盖现有文件：

`bzip2 --force {{path/to/compressed_file.bz2}}`

- 显示帮助信息：

`bzip2 -h`