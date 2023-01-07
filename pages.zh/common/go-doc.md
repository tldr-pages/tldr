# go doc

> 显示包或符号的文档。
> 更多信息：<https://golang.org/cmd/go/#hdr-Show_documentation_for_package_or_symbol>.

- 显示当前包的文档：

`go doc`

- 显示包文档及导出符号：

`go doc {{encoding/json}}`

- 同时显示符号的文档：

`go doc -all {{encoding/json}}`

- 同时显示源代码：

`go doc -all -src {{encoding/json}}`

- 显示指定的符号：

`go doc -all -src {{encoding/json.Number}}`
