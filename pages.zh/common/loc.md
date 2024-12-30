# loc

> 计数代码行数。用 Rust 编写。
> 更多信息：<https://github.com/cgag/loc>。

- 打印当前目录的代码行数：

`loc`

- 打印目标目录的代码行数：

`loc {{path/to/directory}}`

- 打印各个文件的代码行数及统计信息：

`loc --files`

- 打印不包含 .gitignore（等）文件的代码行数（例如，使用两个 -u 标志将额外计算隐藏文件和目录）：

`loc -u`