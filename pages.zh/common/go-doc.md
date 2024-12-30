# go doc

> 查看包或符号的文档。
> 更多信息：<https://golang.org/cmd/go/#hdr-Show_documentation_for_package_or_symbol>。

- 查看当前包的文档：

`go doc`

- 显示包文档和已导出的符号：

`go doc {{encoding/json}}`

- 还显示符号的文档：

`go doc -all {{encoding/json}}`

- 还显示源代码：

`go doc -all -src {{encoding/json}}`

- 显示特定符号：

`go doc -all -src {{encoding/json.Number}}`