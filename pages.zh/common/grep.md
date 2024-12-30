# grep

> 使用正则表达式在文件中查找模式。
> 更多信息：<https://www.gnu.org/software/grep/manual/grep.html>。

- 在文件中搜索模式：

`grep "{{search_pattern}}" {{path/to/file}}`

- 搜索确切字符串（禁用正则表达式）：

`grep {{-F|--fixed-strings}} "{{exact_string}}" {{path/to/file}}`

- 在目录中递归搜索所有文件中的模式，显示匹配行的行号，忽略二进制文件：

`grep {{-r|--recursive}} {{-n|--line-number}} --binary-files {{without-match}} "{{search_pattern}}" {{path/to/directory}}`

- 使用扩展正则表达式（支持 `?`、`+`、`{}`、`()` 和 `|`），以不区分大小写的模式：

`grep {{-E|--extended-regexp}} {{-i|--ignore-case}} "{{search_pattern}}" {{path/to/file}}`

- 打印每个匹配项上下文的3行内容，或在匹配项之前或之后的内容：

`grep --{{context|before-context|after-context}} 3 "{{search_pattern}}" {{path/to/file}}`

- 对于每个匹配项打印文件名和行号，并带有颜色输出：

`grep {{-H|--with-filename}} {{-n|--line-number}} --color=always "{{search_pattern}}" {{path/to/file}}`

- 搜索匹配模式的行，仅打印匹配文本：

`grep {{-o|--only-matching}} "{{search_pattern}}" {{path/to/file}}`

- 在 `stdin` 中搜索不匹配模式的行：

`cat {{path/to/file}} | grep {{-v|--invert-match}} "{{search_pattern}}"`