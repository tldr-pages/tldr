# zipgrep

> 使用扩展正则表达式（支持 `?`、`+`、`{}`、`()` 和 `|`）在 Zip 归档文件中查找模式。
> 更多信息：<https://manned.org/zipgrep>。

- 在 Zip 归档文件中搜索模式：

`zipgrep "{{search_pattern}}" {{path/to/file.zip}}`

- 对于每个匹配项打印文件名和行号：

`zipgrep -H -n "{{search_pattern}}" {{path/to/file.zip}}`

- 搜索不匹配某个模式的行：

`zipgrep -v "{{search_pattern}}" {{path/to/file.zip}}`

- 从 Zip 归档文件中指定要搜索的文件：

`zipgrep "{{search_pattern}}" {{path/to/file.zip}} {{file/to/search1}} {{file/to/search2}}`

- 从 Zip 归档文件中排除搜索的文件：

`zipgrep "{{search_pattern}}" {{path/to/file.zip}} -x {{file/to/exclude1}} {{file/to/exclude2}}`