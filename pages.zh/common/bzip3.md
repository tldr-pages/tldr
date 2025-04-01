# bzip3

> 一个高效的统计文件压缩工具。
> 更多信息：<https://manned.org/bzip3>.

- 压缩文件：

`bzip3 {{path/to/file_to_compress}}`

- 解压缩文件：

`bzip3 {{[-d|--decode]}} {{path/to/compressed_file.bz3}}`

- 将文件解压缩到 `stdout` ([c])：

`bzip3 {{[-dc|--decode --stdout]}} {{path/to/compressed_file.bz3}}`

- 测试归档文件中每个文件的完整性：

`bzip3 {{[-t|--test]}} {{path/to/compressed_file.bz3}}`

- 显示每个处理文件的压缩比率及其详细信息：

`bzip3 {{[-v|--verbose]}} {{path/to/compressed_files.bz3}}`

- 解压缩文件并覆盖现有文件：

`bzip3 {{[-d|--decode]}} {{[-f--force]}} {{path/to/compressed_file.bz3}}`

- 显示帮助：

`bzip3 {{[-h|--help]}}`