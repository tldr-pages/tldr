# tokei

> 显示代码的统计信息。
> 更多信息：<https://github.com/XAMPPRocky/tokei>。

- 显示目录及其所有子目录中的代码报告：

`tokei {{path/to/directory}}`

- 显示目录中的报告，但排除 `.min.js` 文件：

`tokei {{path/to/directory}} -e {{*.min.js}}`

- 显示目录中每个文件的统计信息：

`tokei {{path/to/directory}} --files`

- 显示所有 Rust 和 Markdown 文件类型的报告：

`tokei {{path/to/directory}} -t={{Rust}},{{Markdown}}`