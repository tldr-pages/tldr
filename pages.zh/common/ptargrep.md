# ptargrep

> 在 tar 归档文件中查找正则表达式模式。
> 更多信息：<https://manned.org/ptargrep>。

- 在一个或多个 tar 归档文件中搜索模式：

`ptargrep "{{search_pattern}}" {{path/to/file1 path/to/file2 ...}}`

- 使用归档文件中的文件基名提取到当前目录：

`ptargrep --basename "{{search_pattern}}" {{path/to/file}}`

- 在 tar 归档文件中搜索不区分大小写的模式匹配：

`ptargrep --ignore-case "{{search_pattern}}" {{path/to/file}}`
