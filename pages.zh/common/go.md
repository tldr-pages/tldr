# Go

> 管理 Go 源代码。
> 一些子命令，例如 `build`，有自己的使用文档。
> 更多信息：<https://golang.org>。

- 下载并安装指定的包，使用其导入路径：

`go get {{package_path}}`

- 编译并运行源文件（必须包含 `main` 包）：

`go run {{file}}.go`

- 将源文件编译为命名可执行文件：

`go build -o {{executable}} {{file}}.go`

- 编译当前目录中的包：

`go build`

- 执行当前包的所有测试用例（文件必须以 `_test.go` 结尾）：

`go test`

- 编译并安装当前包：

`go install`

- 在当前目录初始化一个新模块：

`go mod init {{module_name}}`