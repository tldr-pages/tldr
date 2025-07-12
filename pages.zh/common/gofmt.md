# gofmt

> 格式化 Go 源代码。
> 更多信息：<https://pkg.go.dev/cmd/gofmt>.

- 格式化文件并在控制台输出结果：

`gofmt {{源代码.go}}`

- 格式化文件并覆盖原文件：

`gofmt -w {{源代码.go}}`

- 格式化文件和简化代码并覆盖原文件：

`gofmt -s -w {{源代码.go}}`

- 打印所有（包括虚假的）错误：

`gofmt -e {{源代码.go}}`
