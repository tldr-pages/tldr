# zpaq

> 增量日志备份工具和归档器。
> 更多信息：<https://mattmahoney.net/dc/zpaq.html>。

- [a] 将文件或目录添加到新建或现有的归档中：

`zpaq a {{path/to/archive.zpaq}} {{path/to/file_or_directory}}`

- 创建或添加到加密归档中：

`zpaq a -k{{password}} {{path/to/archive.zpaq}} {{path/to/file_or_directory}}`

- E[x]提取文件的最新版本：

`zpaq x {{path/to/archive.zpaq}}`

- [l] 列出归档内容：

`zpaq l {{path/to/archive.zpaq}}`

- 设置压缩级别（级别越高意味着压缩更多但速度较慢）：

`zpaq a {{path/to/archive.zpaq}} -m{{1|2|3|4|5}} {{path/to/file_or_directory}}`

- E[x]提取归档中指定的文件，这些文件不晚于指定日期：

`zpaq x {{path/to/archive.zpaq}} {{path/in/archive/to/extract}} -to {{path/to/output}} -until {{YYYY-MM-DD}}`