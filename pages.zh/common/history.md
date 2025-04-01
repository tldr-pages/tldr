# history

> 命令行历史记录。
> 更多信息：<https://www.gnu.org/software/bash/manual/html_node/Bash-History-Builtins.html#index-history>.

- 显示带行号的命令历史列表：

`history`

- 显示最后 20 条命令（在 Zsh 中显示从第 20 条开始的所有命令）：

`history {{20}}`

- 以不同格式显示带时间戳的历史记录（仅在 Zsh 中可用）：

`history -{{d|f|i|E}}`

- [c]lear 清除命令历史列表（仅限当前 Bash shell）：

`history -c`

- Over[w]rite 用当前 Bash shell 的历史记录覆盖历史文件（通常与 `history -c` 结合使用以清除历史记录）：

`history -w`

- [d]elete 删除指定偏移量的历史记录条目：

`history -d {{offset}}`