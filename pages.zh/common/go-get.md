# go get

> 添加依赖包，或在旧版 GOPATH 模式下下载包。
> 更多信息：<https://pkg.go.dev/cmd/go#hdr-Add_dependencies_to_current_module_and_install_them>.

- 在模块模式下将指定包添加到 `go.mod`，或在 GOPATH 模式下安装包：

`go get {{example.com/pkg}}`

- 在模块感知模式下使用指定版本修改包：

`go get {{example.com/pkg}}@{{v1.2.3}}`

- 移除指定包：

`go get {{example.com/pkg}}@{{none}}`
