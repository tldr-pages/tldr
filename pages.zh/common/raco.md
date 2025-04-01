# raco

> Racket 命令行工具。
> 更多信息：<https://docs.racket-lang.org/raco/>.

- 安装一个包，自动安装依赖项：

`raco pkg install --auto {{package_source}}`

- 将当前目录安装为一个包：

`raco pkg install`

- 为集合构建（或重新构建）字节码、文档、可执行文件和元数据索引：

`raco setup {{collection1 collection2 ...}}`

- 运行文件中的测试：

`raco test {{path/to/tests1.rkt path/to/tests2.rkt ...}}`

- 搜索本地文档：

`raco docs {{search_terms ...}}`

- 显示帮助：

`raco help`
