# cmp

> 逐字节比较两个文件。
> 更多信息：<https://www.gnu.org/software/diffutils/manual/html_node/Invoking-cmp.html>。

- 输出两个文件之间第一个差异的字符和行号：

`cmp {{path/to/file1}} {{path/to/file2}}`

- 输出第一个差异的信息：字符、行号、字节和数值：

`cmp --print-bytes {{path/to/file1}} {{path/to/file2}}`

- 输出每个差异的字节号码和数值：

`cmp --verbose {{path/to/file1}} {{path/to/file2}}`

- 比较文件但不输出任何内容，仅返回退出状态：

`cmp --quiet {{path/to/file1}} {{path/to/file2}}`