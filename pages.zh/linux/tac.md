# tac

> 以反向顺序显示和连接文件的行。
> 另见：`cat`。
> 更多信息：<https://www.gnu.org/software/coreutils/tac>。

- 以反向顺序连接特定文件：

`tac {{path/to/file1 path/to/file2 ...}}`

- 以反向顺序显示 `stdin`：

`{{cat path/to/file}} | tac`

- 使用特定的分隔符：

`tac --separator {{,}} {{path/to/file1 path/to/file2 ...}}`

- 使用特定的正则表达式作为分隔符：

`tac --regex --separator {{[,;]}} {{path/to/file1 path/to/file2 ...}}`

- 在每个文件之前使用分隔符：

`tac --before {{path/to/file1 path/to/file2 ...}}`