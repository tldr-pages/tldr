# mimetype

> 自动确定文件的 MIME 类型。
> 更多信息：<https://manned.org/mimetype>。

- 打印给定文件的 MIME 类型：

`mimetype {{path/to/file}}`

- 仅显示 MIME 类型，不显示文件名：

`mimetype --brief {{path/to/file}}`

- 显示 MIME 类型的描述：

`mimetype --describe {{path/to/file}}`

- 确定 `stdin` 的 MIME 类型（不检查文件名）：

`{{command}} | mimetype --stdin`

- 显示确定 MIME 类型的调试信息：

`mimetype --debug {{path/to/file}}`

- 按置信度顺序显示给定文件的所有可能的 MIME 类型：

`mimetype --all {{path/to/file}}`

- 显式指定输出的双字母语言代码：

`mimetype --language {{path/to/file}}`