# history

> 管理命令行历史记录。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-history>。

- 显示带行号的命令历史列表：

`history`

- 显示最后 20 条命令（在 Zsh 中显示从第 20 条开始的所有命令）：

`history 20`

- 以不同格式显示带时间戳的历史记录（仅在 Zsh 中可用）：

`history -{{d|f|i|E}}`

- 清除命令历史列表：

`history -c`

- 用当前 Bash shell 的历史记录覆盖历史文件（通常与 `history -c` 结合使用以清除历史）：

`history -w`

- 删除指定偏移量的历史条目：

`history -d {{偏移量}}`

- 将命令添加到历史记录而不运行它：

`history -s {{命令}}`

- 通过添加前导空格运行命令而不将其添加到历史记录：

`<Space>{{命令}}`
