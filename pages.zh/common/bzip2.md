# bzip2

> 一个基于块排序的文件压缩工具。
> 更多信息：<https://manned.org/bzip2>.

- 压缩文件：

`bzip2 {{path/to/file_to_compress}}`

- 解压缩文件：

`bzip2 {{[-d|--decompress]}} {{path/to/compressed_file.bz2}}`

- 将解压缩内容输出到 `stdout`：

`bzip2 {{[-dc|--decompress --stdout]}} {{path/to/compressed_file.bz2}}`

- 测试存档文件中每个文件的完整性：

`bzip2 {{[-t|--test]}} {{path/to/compressed_file.bz2}}`

- 显示每个处理文件的压缩比及详细信息：

`bzip2 {{[-v|--verbose]}} {{path/to/compressed_files.bz2}}`

- 解压缩文件并覆盖现有文件：

`bzip2 {{[-f|--force]}} {{path/to/compressed_file.bz2}}`

- 显示帮助信息：

`bzip2 {{[-h|--help]}}`