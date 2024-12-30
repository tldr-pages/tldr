# 历史

> 命令行历史。
> 更多信息：<https://www.gnu.org/software/bash/manual/html_node/Bash-History-Builtins.html>。

- 以行号显示命令历史列表：

`history`

- 显示最后 20 个命令（在 Zsh 中，从第 20 个开始显示所有命令）：

`history {{20}}`

- 以不同格式显示带时间戳的历史（仅在 Zsh 中可用）：

`history -{{d|f|i|E}}`

- [c]lear 当前 Bash shell 的命令历史列表：

`history -c`

- 用当前 Bash shell 的历史覆盖历史文件（通常与 `history -c` 结合使用以清除历史）：

`history -w`

- [d]elete 指定偏移量的历史条目：

`history -d {{offset}}`