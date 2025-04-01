# gofmt

> 格式化 Go 源代码。
> 更多信息：<https://golang.org/cmd/gofmt/>.

- 格式化文件并将结果输出到控制台：

`gofmt {{source.go}}`

- 格式化文件，覆盖原文件：

`gofmt -w {{source.go}}`

- 格式化文件并简化代码，覆盖原文件：

`gofmt -s -w {{source.go}}`

- 打印所有（包括虚假的）错误：

`gofmt -e {{source.go}}`