# 历史扩展

> 在 `sh`、Bash、Zsh、`rbash` 和 `ksh` 中重用和扩展 shell 历史。
> 更多信息：<https://www.gnu.org/software/bash/manual/html_node/History-Interaction>。

- 以 root 身份运行上一个命令（`!!` 被上一个命令替换）：

`sudo !!`

- 使用上一个命令的最后一个参数运行命令：

`{{command}} !$`

- 使用上一个命令的第一个参数运行命令：

`{{command}} !^`

- 运行历史中的第 N 个命令：

`!{{n}}`

- 运行历史中向前 n 行的命令：

`!-{{n}}`

- 运行最近包含 `string` 的命令：

`!?{{string}}?`

- 运行上一个命令，将 `string1` 替换为 `string2`：

`^{{string1}}^{{string2}}^`

- 执行历史扩展，但打印将要运行的命令，而不实际运行它：

`{{!-n}}:p`