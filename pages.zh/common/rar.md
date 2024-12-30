# rar

> RAR归档工具。支持可以选择自解压的多卷归档。
> 更多信息：<https://manned.org/rar>。

- 归档1个或多个文件：

`rar a {{path/to/archive_name.rar}} {{path/to/file1}} {{path/to/file2}} {{path/to/file3}}`

- 归档一个目录：

`rar a {{path/to/archive_name.rar}} {{path/to/directory}}`

- 将归档分割成相等大小的多个部分（50M）：

`rar a -v{{50M}} -R {{path/to/archive_name.rar}} {{path/to/file_or_directory}}`

- 为生成的归档设置密码保护：

`rar a -p{{password}} {{path/to/archive_name.rar}} {{path/to/file_or_directory}}`

- 使用密码加密文件数据和头部信息：

`rar a -hp{{password}} {{path/to/archive_name.rar}} {{path/to/file_or_directory}}`

- 使用特定的压缩级别（0-5）：

`rar a -m{{compression_level}} {{path/to/archive_name.rar}} {{path/to/file_or_directory}}`