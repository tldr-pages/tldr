# json5

> 将 JSON5 文件转换为 JSON。
> 更多信息：<https://json5.org>。

- 将 JSON5 `stdin` 转换为 JSON `stdout`：

`echo {{input}} | json5`

- 将 JSON5 文件转换为 JSON 并输出到 `stdout`：

`json5 {{path/to/input_file.json5}}`

- 将 JSON5 文件转换为指定的 JSON 文件：

`json5 {{path/to/input_file.json5}} --out-file {{path/to/output_file.json}}`

- 验证 JSON5 文件：

`json5 {{path/to/input_file.json5}} --validate`

- 指定缩进的空格数（或使用 "t" 表示制表符）：

`json5 --space {{indent_amount}}`

- 显示帮助信息：

`json5 --help`