# rar

> RAR 归档工具。支持多卷归档，可以是自解压的。
> 更多信息：<https://manned.org/rar>。

- 将 1 个或多个文件归档：

`rar a {{path/to/archive_name.rar}} {{path/to/file1}} {{path/to/file2}} {{path/to/file3}}`

- 将一个目录归档：

`rar a {{path/to/archive_name.rar}} {{path/to/directory}}`

- 将归档文件分割成等大小的部分（50M）：

`rar a -v{{50M}} -R {{path/to/archive_name.rar}} {{path/to/file_or_directory}}`

- 为归档文件设置密码保护：

`rar a -p{{password}} {{path/to/archive_name.rar}} {{path/to/file_or_directory}}`

- 使用密码加密文件数据和头部信息：

`rar a -hp{{password}} {{path/to/archive_name.rar}} {{path/to/file_or_directory}}`

- 使用特定的压缩级别（0-5）：

`rar a -m{{compression_level}} {{path/to/archive_name.rar}} {{path/to/file_or_directory}}`