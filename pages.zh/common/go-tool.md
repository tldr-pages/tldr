# go tool

> 运行 Go 工具或命令。
> 以独立二进制文件形式执行 Go 命令，通常用于调试。
> 更多信息：<https://pkg.go.dev/cmd/go#hdr-Run_specified_go_tool>。

- 列出可用的工具：

`go tool`

- 运行 go 链接工具：

`go tool link {{path/to/main.o}}`

- 打印将要执行的命令，但不执行它（类似于 `whereis`）：

`go tool -n {{command}} {{arguments}}`

- 查看指定工具的文档：

`go tool {{command}} --help`

- 列出所有可用的交叉编译目标：

`go tool dist list`