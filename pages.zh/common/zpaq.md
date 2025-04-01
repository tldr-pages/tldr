# zpaq

> 增量日志备份工具和归档工具。
> 更多信息：<https://mattmahoney.net/dc/zpaqdoc.html>。

- 向新的或现有的归档文件中添加文件或目录：

`zpaq {{[a|add]}} {{path/to/archive.zpaq}} {{path/to/file_or_directory}}`

- 创建或添加到加密归档文件中：

`zpaq {{[a|add]}} -k{{password}} {{path/to/archive.zpaq}} {{path/to/file_or_directory}}`

- 提取归档文件中的最新版本文件：

`zpaq {{[x|extract]}} {{path/to/archive.zpaq}}`

- 列出归档文件的内容：

`zpaq {{[l|list]}} {{path/to/archive.zpaq}}`

- 设置压缩级别（级别越高，压缩效果越好但速度越慢）：

`zpaq {{[a|add]}} {{path/to/archive.zpaq}} -m{{1|2|3|4|5}} {{path/to/file_or_directory}}`

- 从归档文件中提取指定文件，这些文件的修改日期不晚于指定日期：

`zpaq {{[x|extract]}} {{path/to/archive.zpaq}} {{path/in/archive/to/extract}} -to {{path/to/output}} -until {{YYYY-MM-DD}}`