# loc

> 统计代码行数。使用 Rust 编写。
> 更多信息：<https://github.com/cgag/loc>.

- 打印当前目录中的代码行数：

`loc`

- 打印指定目录中的代码行数：

`loc {{path/to/directory}}`

- 打印代码行数并显示每个文件的统计信息：

`loc --files`

- 打印代码行数，不包括 .gitignore（等）文件（例如，两个 -u 标志还会统计隐藏文件和目录）：

`loc -u`
