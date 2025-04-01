# go vet

> 检查 Go 源代码并报告可疑构造（例如，检查 Go 源文件）。
> 如果发现问题，Go vet 返回非零退出代码；如果没有发现问题，则返回零退出代码。
> 更多信息：<https://pkg.go.dev/cmd/vet>。

- 检查当前目录中的 Go 包：

`go vet`

- 检查指定路径中的 Go 包：

`go vet {{path/to/file_or_directory}}`

- 列出可以用 go vet 运行的所有检查：

`go tool vet help`

- 查看特定检查的详细信息和标志：

`go tool vet help {{check_name}}`

- 显示违规行及其上下文的 `n` 行：

`go vet -c={{n}}`

- 以 JSON 格式输出分析和错误：

`go vet -json`