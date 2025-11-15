# json5

> 将 JSON5 文件转换为 JSON。
> 更多信息：<https://json5.org>.

- 将 JSON5 `标准输入` 转换为 JSON 并输出到 `标准输出`：

`echo {{输入}} | json5`

- 将 JSON5 文件转换为 JSON 并输出到 `标准输出`：

`json5 {{路径/到/输入文件.json5}}`

- 将 JSON5 文件转换为指定的 JSON 文件：

`json5 {{路径/到/输入文件.json5}} --out-file {{路径/到/输出文件.json}}`

- 验证一个 JSON5 文件：

`json5 {{路径/到/输入文件.json5}} --validate`

- 指定缩进的空格数（或使用 "t" 表示制表符）：

`json5 --space {{缩进量}}`

- 显示帮助：

`json5 --help`
