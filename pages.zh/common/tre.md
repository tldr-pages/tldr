# tre

> 以树状图形式显示当前目录的内容。
> 默认情况下遵循 `.gitignore` 设置。
> 更多信息：<https://github.com/dduan/tre>.

- 仅打印目录：

`tre --directories`

- 以 JSON 格式打印树状目录结构中的文件，而非正常的树状图：

`tre --json`

- 打印指定深度以内的文件和目录（1 表示当前目录）：

`tre --limit {{depth}}`

- 使用指定的颜色模式打印所有隐藏文件和目录：

`tre --all --color {{automatic|always|never}}`

- 打印树状目录结构中的文件，并为每个文件分配一个 shell 别名，调用时会使用提供的 `command`（默认为 `$EDITOR`）打开文件：

`tre --editor {{command}}`

- 打印树状目录结构中的文件，排除所有匹配提供的正则表达式的路径：

`tre --exclude {{regular_expression}}`

- 显示版本：

`tre --version`

- 显示帮助：

`tre --help`