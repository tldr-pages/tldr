# bzip3

> 一个高效的统计文件压缩工具。
> 更多信息：<https://github.com/kspalaiologos/bzip3>。

- 压缩文件:

`bzip3 {{path/to/file_to_compress}}`

- [解]压缩文件:

`bzip3 -d {{path/to/compressed_file.bz3}}`

- 解压缩文件到 `stdout` ([c]):

`bzip3 -dc {{path/to/compressed_file.bz3}}`

- 测试归档文件中每个文件的完整性:

`bzip3 --test {{path/to/compressed_file.bz3}}`

- 显示每个处理文件的压缩比以及详细信息:

`bzip3 --verbose {{path/to/compressed_files.bz3}}`

- 解压缩文件并覆盖现有文件:

`bzip3 -d --force {{path/to/compressed_file.bz3}}`

- 显示帮助信息:

`bzip3 -h`