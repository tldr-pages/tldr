# nl

> 为文件或 `stdin` 的行编号。
> 更多信息：<https://manned.org/nl.1p>.

- 为文件中的非空行编号：

`nl {{path/to/file}}`

- 从 `stdin` 读取：

`{{command}} | nl -`

- 为所有正文行（包括空白行）编号或不为正文行编号：

`nl -b {{a|n}} {{path/to/file}}`

- 仅对匹配基本正则表达式 (BRE) 模式的正文行编号：

`nl -b p'FooBar[0-9]' {{path/to/file}}`

- 指定行编号的增量：

`nl -i {{increment}} {{path/to/file}}`

- 指定行编号的格式为右对齐、左对齐，并保留前导零或不保留：

`nl -n {{rz|ln|rn}}`

- 指定行编号的宽度（默认为 6）：

`nl -w {{col_width}} {{path/to/file}}`

- 使用特定的字符串将行号与行内容分隔（默认为制表符）：

`nl -s {{separator}} {{path/to/file}}`