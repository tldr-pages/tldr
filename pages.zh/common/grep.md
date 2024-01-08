# grep

> 使用正则表达式查找文件中的模式。
> 更多信息：<https://www.gnu.org/software/grep/manual/grep.html>.

- 在文件中查找模式：

`grep "{{模式字符串}}" {{路径/到/文件}}`

- 在文件中精确地查找字符串（禁用正则表达式）：

`grep --fixed-strings "{{字符串}}" {{路径/到/文件}}`

- 在指定目录下的所有文件中递归地查找模式，显示匹配的行号并忽略二进制文件：

`grep --recursive --line-number --binary-files={{without-match}} "{{模式字符串}}" {{路径/到/目录}}`

- 使用大小写不敏感的扩展正则表达式（支持 `?`、`+`、`{}`、`()` 和 `|`）：

`grep --extended-regexp --ignore-case "{{模式字符串}}" {{路径/到/文件}}`

- 在每个匹配前后、之前或之后打印 3 行上下文：

`grep --{{context|before-context|after-context}}={{3}} "{{模式字符串}}" {{路径/到/文件}}`

- 以带有颜色的方式，打印每个匹配的文件名和行号：

`grep --with-filename --line-number --color=always "{{模式字符串}}" {{路径/到/文件}}`

- 只打印文件中与模式匹配的行：

`grep --only-matching "{{模式字符串}}" {{路径/到/文件}}`

- 从 `stdin`（标准输入）中查找与模式不匹配的行：

`cat {{路径/到/文件}} | grep --invert-match "{{模式字符串}}"`
