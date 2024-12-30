# tokei

> 显示代码的统计信息。
> 更多信息请访问：<https://github.com/XAMPPRocky/tokei>。

- 显示一个目录及其所有子目录中代码的报告：

`tokei {{path/to/directory}}`

- 显示一个目录的报告，排除 `.min.js` 文件：

`tokei {{path/to/directory}} -e {{*.min.js}}`

- 显示一个目录中单个文件的统计信息：

`tokei {{path/to/directory}} --files`

- 显示所有 Rust 和 Markdown 类型文件的报告：

`tokei {{path/to/directory}} -t={{Rust}},{{Markdown}}`