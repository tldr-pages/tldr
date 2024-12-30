# xzgrep

> 使用正则表达式搜索可能被 `xz`、`lzma`、`gzip`、`bzip2`、`lzop` 或 `zstd` 压缩的文件。
> 另见: `grep`。
> 更多信息: <https://manned.org/xzgrep>。

- 在文件中搜索模式：

`xzgrep "{{search_pattern}}" {{path/to/file}}`

- 搜索确切字符串（禁用正则表达式）：

`xzgrep --fixed-strings "{{exact_string}}" {{path/to/file}}`

- 在所有文件中搜索模式，并显示匹配的行号：

`xzgrep --line-number "{{search_pattern}}" {{path/to/file}}`

- 使用扩展正则表达式（支持 `?`、`+`、`{}`、`()` 和 `|`），以不区分大小写的模式：

`xzgrep --extended-regexp --ignore-case "{{search_pattern}}" {{path/to/file}}`

- 打印每个匹配前后各3行的上下文：

`xzgrep --{{context|before-context|after-context}}={{3}} "{{search_pattern}}" {{path/to/file}}`

- 打印每个匹配的文件名和行号，并使用彩色输出：

`xzgrep --with-filename --line-number --color=always "{{search_pattern}}" {{path/to/file}}`

- 搜索匹配模式的行，仅打印匹配的文本：

`xzgrep --only-matching "{{search_pattern}}" {{path/to/file}}`