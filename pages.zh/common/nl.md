# nl

> 从文件或 `stdin` 中编号行。
> 更多信息：<https://manned.org/nl.1p>。

- 编号文件中的非空行：

`nl {{path/to/file}}`

- 从 `stdin` 读取：

`{{command}} | nl -`

- 编号[a]ll[b]ody 行，包括空行，或不编号[b]ody 行：

`nl -b {{a|n}} {{path/to/file}}`

- 仅编号与基本正则表达式（BRE）[p]attern 匹配的[b]ody 行：

`nl -b p'FooBar[0-9]' {{path/to/file}}`

- 使用特定的[i]ncrement 进行行编号：

`nl -i {{increment}} {{path/to/file}}`

- 指定行编号格式为[r]ight 或[l]eft 对齐，保留前导[z]eros 或不保留：

`nl -n {{rz|ln|rn}}`

- 指定行编号的[w]idth（默认6）：

`nl -w {{col_width}} {{path/to/file}}`

- 使用特定字符串[s]eparate 行号与行（默认使用 TAB）：

`nl -s {{separator}} {{path/to/file}}`