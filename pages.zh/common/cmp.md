# cmp

> 逐字节比较两个文件。
> 更多信息：<https://www.gnu.org/software/diffutils/manual/html_node/Invoking-cmp.html>.

- 输出两个文件第一个差异的字符和行号：

`cmp {{path/to/file1}} {{path/to/file2}}`

- 输出第一个差异的详细信息：字符、行号、字节和值：

`cmp {{[-b|--print-bytes]}} {{path/to/file1}} {{path/to/file2}}`

- 输出每个差异的字节编号和值：

`cmp {{[-l|--verbose]}} {{path/to/file1}} {{path/to/file2}}`

- 比较文件但不输出任何内容，仅提供退出状态：

`cmp {{[-s|--quiet]}} {{path/to/file1}} {{path/to/file2}}`
