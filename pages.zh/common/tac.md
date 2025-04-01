# tac

> 以反向顺序显示和连接文件行。
> 参见：`cat`。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/tac-invocation.html>.

- 以反向顺序连接指定文件：

`tac {{path/to/file1 path/to/file2 ...}}`

- 以反向顺序显示 `stdin`：

`{{cat path/to/file}} | tac`

- 使用特定分隔符：

`tac {{[-s|--separator]}} {{separator}} {{path/to/file1 path/to/file2 ...}}`

- 使用特定正则表达式作为分隔符：

`tac {{[-r|--regex]}} {{[-s|--separator]}} {{separator}} {{path/to/file1 path/to/file2 ...}}`

- 在每个文件前使用分隔符：

`tac {{[-b|--before]}} {{path/to/file1 path/to/file2 ...}}`