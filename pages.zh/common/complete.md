# 完成

> 获取对 shell 命令的参数自动补全。
> 更多信息：<https://www.gnu.org/software/bash/manual/html_node/Programmable-Completion-Builtins.html>。

- 将执行自动补全的函数应用于命令：

`complete -F {{function}} {{command}}`

- 将执行自动补全的命令应用于另一个命令：

`complete -C {{autocomplete_command}} {{command}}`

- 应用自动补全而不在补全的单词后附加空格：

`complete -o nospace -F {{function}} {{command}}`