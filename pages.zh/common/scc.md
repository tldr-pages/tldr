# scc

> 统计代码行数。使用 Go 编写。
> 更多信息：<https://github.com/boyter/scc>。

- 打印当前目录的代码行数：

`scc`

- 打印目标目录的代码行数：

`scc {{path/to/directory}}`

- 显示每个文件的输出：

`scc --by-file`

- 使用特定的输出格式显示输出（默认为 `tabular`）：

`scc --format {{tabular|wide|json|csv|cloc-yaml|html|html-table}}`

- 仅统计具有特定文件扩展名的文件：

`scc --include-ext {{go,java,js}}`

- 排除目录不被统计：

`scc --exclude-dir {{.git,.hg}}`

- 显示输出并按列排序（默认为按文件排序）：

`scc --sort {{files|name|lines|blanks|code|comments|complexity}}`

- 显示帮助信息：

`scc -h`