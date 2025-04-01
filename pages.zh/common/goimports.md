# goimports

> 更新 Go 导入行，添加缺失的导入并移除未引用的导入。
> 更多信息：<https://godoc.org/golang.org/x/tools/cmd/goimports>。

- 显示完成导入的源文件：

`goimports {{path/to/file.go}}`

- 将结果写回源文件而不是 `stdout`：

`goimports -w {{path/to/file.go}}`

- 显示差异并将结果写回源文件：

`goimports -w -d {{path/to/file.go}}`

- 设置第三方包后的导入前缀字符串（逗号分隔列表）：

`goimports -local {{path/to/package1,path/to/package2,...}} {{path/to/file.go}}`