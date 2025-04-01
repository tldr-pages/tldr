# godoc

> 查看 Go 包的文档。
> 更多信息：<https://godoc.org/>.

- 显示特定包的帮助信息：

`godoc {{fmt}}`

- 显示 "fmt" 包中 "Printf" 函数的帮助信息：

`godoc {{fmt}} {{Printf}}`

- 作为 web 服务器在端口 6060 上提供文档服务：

`godoc -http=:{{6060}}`

- 创建索引文件：

`godoc -write_index -index_files={{path/to/file}}`

- 使用指定的索引文件搜索文档：

`godoc -http=:{{6060}} -index -index_files={{path/to/file}}`
