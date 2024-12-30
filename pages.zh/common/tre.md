# tre

> 以树形结构显示当前目录的内容。
> 默认情况下遵循 `.gitignore` 设置。
> 更多信息：<https://github.com/dduan/tre>。

- 仅打印目录：

`tre --directories`

- 打印包含文件的树形结构的 JSON，而不是正常的树形图：

`tre --json`

- 打印文件和目录，直到指定的深度限制（其中 1 表示当前目录）：

`tre --limit {{depth}}`

- 使用指定的颜色化模式打印所有隐藏的文件和目录：

`tre --all --color {{automatic|always|never}}`

- 打印树形结构中的文件，为每个文件分配一个 shell 别名，当调用时将使用提供的 `command`（或默认在 `$EDITOR` 中）打开相关文件：

`tre --editor {{command}}`

- 打印树形结构中的文件，排除所有与提供的正则表达式匹配的路径：

`tre --exclude {{regular_expression}}`

- 显示版本：

`tre --version`

- 显示帮助：

`tre --help`