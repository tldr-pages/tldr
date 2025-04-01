# bzgrep

> 使用 `grep` 在 `bzip2` 压缩文件中查找模式。
> 更多信息：<https://manned.org/bzgrep>.

- 在压缩文件中查找模式：

`bzgrep "{{search_pattern}}" {{path/to/file}}`

- 使用扩展正则表达式（支持 `?`, `+`, `{}`, `()` 和 `|`），并以不区分大小写模式进行搜索：

`bzgrep --extended-regexp --ignore-case "{{search_pattern}}" {{path/to/file}}`

- 打印每个匹配项的上下文、之前或之后的 3 行：

`bzgrep --{{context|before-context|after-context}}={{3}} "{{search_pattern}}" {{path/to/file}}`

- 打印每个匹配项的文件名和行号：

`bzgrep --with-filename --line-number "{{search_pattern}}" {{path/to/file}}`

- 搜索与模式匹配的行，仅打印匹配的文本：

`bzgrep --only-matching "{{search_pattern}}" {{path/to/file}}`

- 递归地在 bzip2 压缩的 tar 归档文件中搜索模式：

`bzgrep --recursive "{{search_pattern}}" {{path/to/tar/file}}`

- 从 `stdin` 中搜索不匹配模式的行：

`cat {{/path/to/bz/compressed/file}} | bzgrep --invert-match "{{search_pattern}}"`
