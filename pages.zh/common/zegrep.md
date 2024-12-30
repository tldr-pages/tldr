# zegrep

> 使用 `egrep` 在压缩文件中查找扩展正则表达式模式。
> 更多信息：<https://www.unix.com/man-page/freebsd/1/zegrep/>

- 在压缩文件中搜索扩展正则表达式（支持 `?`、`+`、`{}`、`()` 和 `|`，区分大小写）：

`zegrep "{{search_pattern}}" {{path/to/file}}`

- 在压缩文件中搜索扩展正则表达式（支持 `?`、`+`、`{}`、`()` 和 `|`，不区分大小写）：

`zegrep --ignore-case "{{search_pattern}}" {{path/to/file}}`

- 搜索不匹配某个模式的行：

`zegrep --invert-match "{{search_pattern}}" {{path/to/file}}`

- 对于每个匹配项打印文件名和行号：

`zegrep --with-filename --line-number "{{search_pattern}}" {{path/to/file}}`

- 搜索匹配某个模式的行，仅打印匹配的文本：

`zegrep --only-matching "{{search_pattern}}" {{path/to/file}}`

- 在压缩文件中递归搜索某个模式的文件：

`zegrep --recursive "{{search_pattern}}" {{path/to/file}}`