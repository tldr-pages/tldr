# go vet

> 检查 Go 源代码并报告可疑的构造（例如，对你的 Go 源文件进行 lint 检查）。
> 如果发现问题，Go vet 返回非零退出代码；如果没有发现问题，则返回零退出代码。
> 更多信息：<https://pkg.go.dev/cmd/vet>。

- 检查当前目录中的 Go 包：

`go vet`

- 检查指定路径中的 Go 包：

`go vet {{path/to/file_or_directory}}`

- 列出可以与 go vet 一起运行的可用检查：

`go tool vet help`

- 查看特定检查的详细信息和标志：

`go tool vet help {{check_name}}`

- 显示有问题的行以及 N 行周围的上下文：

`go vet -c={{N}}`

- 以 JSON 格式输出分析和错误：

`go vet -json`