# nl

> 为文件或从 `stdin` 读取的内容加上行号。
> 更多信息：<https://manned.org/nl>.

- 为文件中的非空白行编号：

`nl {{path/to/file}}`

- 从 `stdin` 读取内容：

`{{command}} | nl -`

- 为正文中的所有行（包括空白行）编号或不为正文行编号：

`nl {{[-b|--body-numbering]}} {{a|n}} {{path/to/file}}`

- 仅对匹配基本正则表达式 (BRE) [p]attern 的正文行编号：

`nl {{[-b|--body-numbering]}} p'FooBar[0-9]' {{path/to/file}}`

- 为行号使用特定的递增值：

`nl {{[-i|--line-increment]}} {{increment}} {{path/to/file}}`

- 指定行号的格式，右对齐 [r]，左对齐 [l]，保持前导零 [z] 或不保持 [n]：

`nl {{[-n|--number-format]}} {{rz|ln|rn}}`

- 指定行号的宽度（默认为 6）：

`nl {{[-w|--number-width]}} {{col_width}} {{path/to/file}}`

- 使用特定的字符串将行号与内容分隔开（默认为制表符）：

`nl {{[-s|--number-separator]}} {{separator}} {{path/to/file}}`
