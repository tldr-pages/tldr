# bzegrep

> 使用 `egrep` 在 `bzip2` 压缩文件中查找扩展正则表达式模式。
> 更多信息：<https://manned.org/bzegrep>。

- 在压缩文件中搜索扩展正则表达式（支持 `?`、`+`、`{}`、`()` 和 `|`）（区分大小写）：

`bzegrep "{{search_pattern}}" {{path/to/file}}`

- 在压缩文件中搜索扩展正则表达式（支持 `?`、`+`、`{}`、`()` 和 `|`）（不区分大小写）：

`bzegrep --ignore-case "{{search_pattern}}" {{path/to/file}}`

- 搜索不匹配某模式的行：

`bzegrep --invert-match "{{search_pattern}}" {{path/to/file}}`

- 对于每个匹配，打印文件名和行号：

`bzegrep --with-filename --line-number "{{search_pattern}}" {{path/to/file}}`

- 搜索匹配某模式的行，仅打印匹配的文本：

`bzegrep --only-matching "{{search_pattern}}" {{path/to/file}}`

- 在 bzip2 压缩的 tar 存档中递归搜索文件以查找某模式：

`bzegrep --recursive "{{search_pattern}}" {{path/to/file}}`