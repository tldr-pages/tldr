# go fmt

> 格式化 Go 源代码文件，打印出更改的文件名。
> 更多信息：<https://pkg.go.dev/cmd/go#hdr-Gofmt__reformat__package_sources>.

- 格式化当前目录中的 Go 源代码文件：

`go fmt`

- 格式化指定的 Go 包（在你的导入路径中，例如 `$GOPATH/src`）：

`go fmt {{path/to/package}}`

- 格式化当前目录及其所有子目录中的包（注意 `...`）：

`go fmt {{./...}}`

- 打印格式化命令会运行的内容，但不进行任何修改：

`go fmt -n`

- 在运行格式化命令时打印出运行的命令：

`go fmt -x`