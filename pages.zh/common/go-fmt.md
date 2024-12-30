# go fmt

> 格式化 Go 源文件，并打印更改的文件名。
> 更多信息：<https://pkg.go.dev/cmd/go#hdr-Gofmt__reformat__package_sources>。

- 格式化当前目录中的 Go 源文件：

`go fmt`

- 格式化您导入路径中的特定 Go 包（`$GOPATH/src`）：

`go fmt {{path/to/package}}`

- 格式化当前目录及所有子目录中的包（注意 `...`）：

`go fmt {{./...}}`

- 打印将会运行的格式化命令，而不修改任何内容：

`go fmt -n`

- 打印正在运行的格式化命令：

`go fmt -x`