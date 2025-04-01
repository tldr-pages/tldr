# go test

> 测试 Go 包（文件必须以 `_test.go` 结尾）。
> 更多信息：<https://pkg.go.dev/cmd/go#hdr-Testing_flags>.

- 测试当前目录中的包：

`go test`

- 详细测试当前目录中的包：

`go test -v`

- 测试当前目录及其所有子目录中的包（注意 `...`）：

`go test -v ./...`

- 测试当前目录中的包并运行所有基准测试：

`go test -v -bench .`

- 测试当前目录中的包并运行所有基准测试，持续时间为 50 秒：

`go test -v -bench . -benchtime {{50s}}`

- 以覆盖率分析模式测试包：

`go test -cover`