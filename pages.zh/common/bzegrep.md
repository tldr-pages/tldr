# bzegrep

> 在 `bzip2` 压缩文件中使用 `egrep` 查找扩展正则表达式模式。
> 更多信息：<https://manned.org/bzegrep>.

- 在压缩文件中查找扩展正则表达式（支持 `?`、`+`、`{}`、`()` 和 `|`，区分大小写）：

`bzegrep "{{search_pattern}}" {{path/to/file}}`

- 在压缩文件中查找扩展正则表达式（支持 `?`、`+`、`{}`、`()` 和 `|`，不区分大小写）：

`bzegrep --ignore-case "{{search_pattern}}" {{path/to/file}}`

- 查找不匹配模式的行：

`bzegrep --invert-match "{{search_pattern}}" {{path/to/file}}`

- 为每次匹配打印文件名和行号：

`bzegrep --with-filename --line-number "{{search_pattern}}" {{path/to/file}}`

- 查找匹配模式的行，只打印匹配的文本：

`bzegrep --only-matching "{{search_pattern}}" {{path/to/file}}`

- 递归搜索 bzip2 压缩的 tar 归档文件中的模式：

`bzegrep --recursive "{{search_pattern}}" {{path/to/file}}`