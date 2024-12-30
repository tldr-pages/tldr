# nl

> 从文件或 `stdin` 编号行。
> 更多信息：<https://manned.org/nl.1p>。

- 编号文件中的非空行：

`nl {{path/to/file}}`

- 从 `stdin` 读取：

`{{command}} | nl -`

- 编号所有正文行，包括空行，或不编号正文行：

`nl --body-numbering {{a|n}} {{path/to/file}}`

- 仅编号匹配基本正则表达式（BRE）模式的正文行：

`nl --body-numbering p'FooBar[0-9]' {{path/to/file}}`

- 使用特定增量进行行编号：

`nl --line-increment {{increment}} {{path/to/file}}`

- 指定行编号格式为右对齐或左对齐，保持前导零或不：

`nl --number-format {{rz|ln|rn}}`

- 指定行编号的宽度（默认6）：

`nl --number-width {{col_width}} {{path/to/file}}`

- 使用特定字符串分隔行号和行（默认是TAB）：

`nl --number-separator {{separator}} {{path/to/file}}`