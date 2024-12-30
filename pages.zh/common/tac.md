# tac

> 以反向顺序显示和连接文件的行。
> 另见：`cat`。
> 更多信息：<https://www.gnu.org/software/coreutils/tac>。

- 以反向顺序连接特定文件：

`tac {{path/to/file1 path/to/file2 ...}}`

- 以反向顺序显示 `stdin`：

`{{cat path/to/file}} | tac`

- 使用特定的 [s]eparator：

`tac -s {{separator}} {{path/to/file1 path/to/file2 ...}}`

- 使用特定的 [r]egex 作为 [s]eparator：

`tac -r -s {{separator}} {{path/to/file1 path/to/file2 ...}}`

- 在每个文件之前使用分隔符 [b]：

`tac -b {{path/to/file1 path/to/file2 ...}}`