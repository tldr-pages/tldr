# ptargrep

> 在 tar 压缩文件中查找正则表达式模式。
> 更多信息：<https://manned.org/ptargrep>。

- 在一个或多个 tar 压缩文件中搜索模式：

`ptargrep "{{search_pattern}}" {{path/to/file1 path/to/file2 ...}}`

- 使用来自压缩文件的文件的基本名称提取到当前目录：

`ptargrep --basename "{{search_pattern}}" {{path/to/file}}`

- 在 tar 压缩文件中搜索不区分大小写的匹配模式：

`ptargrep --ignore-case "{{search_pattern}}" {{path/to/file}}`