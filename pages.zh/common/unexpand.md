# unexpand

> 将空格转换为制表符。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/unexpand-invocation.html>.

- 将每个文件中的空格转换为制表符，并写入到 `stdout`：

`unexpand {{路径/到/文件}}`

- 将空格转换为制表符，从 `stdout` 读取：

`unexpand`

- 转换所有空格，而不仅仅是开头的空格：

`unexpand -a {{路径/到/文件}}`

- 仅转换开头的空格序列（覆盖 -a）：

`unexpand --first-only {{路径/到/文件}}`

- 将制表符间隔设置为某个字符数，而不是 8（启用 -a）：

`unexpand -t {{数量}} {{路径/到/文件}}`
