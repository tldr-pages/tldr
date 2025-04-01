# isutf8

> 检查文本文件是否包含有效的 UTF-8。
> 更多信息：<https://joeyh.name/code/moreutils/>.

- 检查指定的文件是否包含有效的 UTF-8：

`isutf8 {{path/to/file1 path/to/file2 ...}}`

- 使用多行输出错误：

`isutf8 --verbose {{path/to/file1 path/to/file2 ...}}`

- 不向 `stdout` 输出任何内容，仅通过退出代码指示结果：

`isutf8 --quiet {{path/to/file1 path/to/file2 ...}}`

- 仅输出包含无效 UTF-8 的文件名：

`isutf8 --list {{path/to/file1 path/to/file2 ...}}`

- 与 `--list` 相反，即仅输出包含有效 UTF-8 的文件名：

`isutf8 --invert {{path/to/file1 path/to/file2 ...}}`
