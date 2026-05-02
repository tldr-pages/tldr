# grep

> 使用 `regex` 式查找文件中的模式。
> 另请参阅：`regex`。
> 更多信息：<https://www.gnu.org/software/grep/manual/grep.html>。

- 在文件中查找模式：

`grep "{{模式字符串}}" {{路径/到/文件1 路径/到/文件2}}`

- 查找精确的字符串（禁用 `regex` 式）：

`grep {{[-F|--fixed-strings]}} "{{字符串}}" {{路径/到/文件}}`

- 在目录中递归查找所有文件中的模式，忽略二进制文件：

`grep {{[-rI|--recursive --binary-files=without-match]}} "{{模式字符串}}" {{路径/到/目录}}`

- 打印每个匹配项周围、之前或之后的 3 行上下文：

`grep {{--context|--before-context|--after-context}} 3 "{{模式字符串}}" {{路径/到/文件}}`

- 打印每个匹配项的文件名和行号，并带彩色输出：

`grep {{[-Hn|--with-filename --line-number]}} --color=always "{{模式字符串}}" {{路径/到/文件}}`

- 仅打印匹配的文本：

`grep {{[-o|--only-matching]}} "{{模式字符串}}" {{路径/到/文件}}`

- 从 `stdin` （标准输入）中读取数据，不打印匹配模式的行：

`cat {{路径/到/文件}} | grep {{[-v|--invert-match]}} "{{模式字符串}}"`

- 使用扩展 `regex` 式（支持 `?`、`+`、`{}`、`()` 和 `|`），不区分大小写模式：

`grep {{[-Ei|--extended-regexp --ignore-case]}} "{{模式字符串}}" {{路径/到/文件}}`
