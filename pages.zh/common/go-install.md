# go install

> 编译并安装由导入路径指定的包。
> 更多信息：<https://pkg.go.dev/cmd/go#hdr-Compile_and_install_packages_and_dependencies>.

- 编译并安装当前包：

`go install`

- 编译并安装特定的本地包：

`go install {{path/to/package}}`

- 安装程序的最新版本，忽略当前目录中的 `go.mod`：

`go install {{golang.org/x/tools/gopls}}@{{latest}}`

- 安装由当前目录中的 `go.mod` 选择的程序版本：

`go install {{golang.org/x/tools/gopls}}`