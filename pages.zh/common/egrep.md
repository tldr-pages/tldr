# egrep

> 使用扩展正则表达式（支持 `?`, `+`, `{}`, `()`, 和 `|`）在文件中查找模式。
> 更多信息：<https://manned.org/egrep>.

- 在文件中搜索模式：

`egrep "{{search_pattern}}" {{path/to/file}}`

- 在多个文件中搜索模式：

`egrep "{{search_pattern}}" {{path/to/file1 path/to/file2 ...}}`

- 在 `stdin` 中搜索模式：

`cat {{path/to/file}} | egrep {{search_pattern}}`

- 为每个匹配项打印文件名和行号：

`egrep --with-filename --line-number "{{search_pattern}}" {{path/to/file}}`

- 在目录中递归搜索所有文件中的模式，忽略二进制文件：

`egrep --recursive --binary-files={{without-match}} "{{search_pattern}}" {{path/to/directory}}`

- 搜索不匹配模式的行：

`egrep --invert-match "{{search_pattern}}" {{path/to/file}}`
