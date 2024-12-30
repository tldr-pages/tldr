# column

> 将 `stdin` 或文件格式化为多列。
> 列在行之前填充；默认分隔符为空格。
> 更多信息：<https://manned.org/column>。

- 为宽度为 30 个字符的显示格式化命令输出：

`printf "header1 header2\nbar foo\n" | column --output-width {{30}}`

- 自动拆分列并在表格格式中自动对齐：

`printf "header1 header2\nbar foo\n" | column --table`

- 为 `--table` 选项指定列分隔符字符（例如，CSV 的 ","）（默认为空格）：

`printf "header1,header2\nbar,foo\n" | column --table --separator {{,}}`

- 在填充列之前填充行：

`printf "header1\nbar\nfoobar\n" | column --output-width {{30}} --fillrows`