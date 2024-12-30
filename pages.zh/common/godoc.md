# godoc

> 查看 Go 包的文档。
> 更多信息：<https://godoc.org/>.

- 显示特定包的帮助：

`godoc {{fmt}}`

- 显示 "fmt" 包的 "Printf" 函数的帮助：

`godoc {{fmt}} {{Printf}}`

- 在 6060 端口作为网络服务器提供文档：

`godoc -http=:{{6060}}`

- 创建索引文件：

`godoc -write_index -index_files={{path/to/file}}`

- 使用给定的索引文件搜索文档：

`godoc -http=:{{6060}} -index -index_files={{path/to/file}}`