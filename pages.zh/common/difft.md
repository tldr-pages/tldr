# difft

> 基于编程语言的语法比较文件或目录。
> 参见: `delta`, `diff`。
> 更多信息: <https://difftastic.wilfred.me.uk/introduction.html>。

- 比较两个文件或目录：

`difft {{path/to/file_or_directory1}} {{path/to/file_or_directory2}}`

- 仅报告文件之间是否存在差异：

`difft --check-only {{path/to/file1}} {{path/to/file2}}`

- 指定显示模式（默认为 `side-by-side`）：

`difft --display {{side-by-side|side-by-side-show-both|inline|json}} {{path/to/file1}} {{path/to/file2}}`

- 比较时忽略注释：

`difft --ignore-comments {{path/to/file1}} {{path/to/file2}}`

- 启用/禁用源代码的语法高亮（默认为 `on`）：

`difft --syntax-highlight {{on|off}} {{path/to/file1}} {{path/to/file2}}`

- 如果文件之间没有差异，则不输出任何内容：

`difft --skip-unchanged {{path/to/file_or_directory1}} {{path/to/file_or_directory2}}`

- 打印工具支持的所有编程语言及其扩展名：

`difft --list-languages`
