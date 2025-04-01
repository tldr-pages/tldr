# scc

> 统计代码行数。用 Go 语言编写。
> 更多信息：<https://github.com/boyter/scc>.

- 打印当前目录中的代码行数：

`scc`

- 打印目标目录中的代码行数：

`scc {{path/to/directory}}`

- 为每个文件显示输出：

`scc --by-file`

- 使用特定的输出格式显示输出（默认为 `tabular`）：

`scc --format {{tabular|wide|json|csv|cloc-yaml|html|html-table}}`

- 仅统计具有特定文件扩展名的文件：

`scc --include-ext {{go,java,js}}`

- 排除不统计的目录：

`scc --exclude-dir {{.git,.hg}}`

- 显示并按列排序输出（默认按文件排序）：

`scc --sort {{files|name|lines|blanks|code|comments|complexity}}`

- 显示帮助：

`scc -h`
