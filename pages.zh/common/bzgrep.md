# bzgrep

> 使用 `grep` 查找 `bzip2` 压缩文件中的模式。
> 更多信息：<https://manned.org/bzgrep>。

- 在压缩文件中搜索模式：

`bzgrep "{{search_pattern}}" {{path/to/file}}`

- 使用扩展正则表达式（支持 `?`、`+`、`{}`、`()` 和 `|`），以不区分大小写的模式：

`bzgrep --extended-regexp --ignore-case "{{search_pattern}}" {{path/to/file}}`

- 打印每个匹配项前后各3行上下文：

`bzgrep --{{context|before-context|after-context}}={{3}} "{{search_pattern}}" {{path/to/file}}`

- 为每个匹配项打印文件名和行号：

`bzgrep --with-filename --line-number "{{search_pattern}}" {{path/to/file}}`

- 搜索匹配模式的行，仅打印匹配的文本：

`bzgrep --only-matching "{{search_pattern}}" {{path/to/file}}`

- 递归搜索 bzip2 压缩的 tar 存档中的文件以查找模式：

`bzgrep --recursive "{{search_pattern}}" {{path/to/tar/file}}`

- 在 `stdin` 中搜索不匹配模式的行：

`cat {{/path/to/bz/compressed/file}} | bzgrep --invert-match "{{search_pattern}}"`