# isutf8

> 检查文本文件是否包含有效的 UTF-8。
> 更多信息：<https://joeyh.name/code/moreutils/>.

- 检查指定的文件是否包含有效的 UTF-8：

`isutf8 {{path/to/file1 path/to/file2 ...}}`

- 使用多行打印错误信息：

`isutf8 --verbose {{path/to/file1 path/to/file2 ...}}`

- 不向 `stdout` 打印任何内容，仅通过退出代码指示结果：

`isutf8 --quiet {{path/to/file1 path/to/file2 ...}}`

- 仅打印包含无效 UTF-8 的文件名：

`isutf8 --list {{path/to/file1 path/to/file2 ...}}`

- 与 `--list` 相同，但反向操作，即仅打印包含有效 UTF-8 的文件名：

`isutf8 --invert {{path/to/file1 path/to/file2 ...}}`