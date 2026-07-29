# tac

> 以逆序显示和连接文件。
> 另请参阅：`cat`。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/tac-invocation.html>。

- 以逆序连接指定文件：

`tac {{路径/到/文件1 路径/到/文件2 ...}}`

- 以逆序显示 `stdin`：

`{{cat 路径/到/文件}} | tac`

- 使用特定的分隔符：

`tac {{[-s|--separator]}} {{分隔符}} {{路径/到/文件1 路径/到/文件2 ...}}`

- 使用特定的 `regex` 作为分隔符：

`tac {{[-r|--regex]}} {{[-s|--separator]}} {{分隔符}} {{路径/到/文件1 路径/到/文件2 ...}}`

- 在每个文件之前添加分隔符：

`tac {{[-b|--before]}} {{路径/到/文件1 路径/到/文件2 ...}}`
