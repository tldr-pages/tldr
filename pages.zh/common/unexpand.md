# unexpand

> 将空格转换为制表符。
> 更多信息：<https://www.gnu.org/software/coreutils/unexpand>。

- 将每个文件中的空格转换为制表符，并写入 `stdout`：

`unexpand {{path/to/file}}`

- 从 `stdout` 读取，转换空格为制表符：

`unexpand`

- 转换所有空格，而不仅仅是开头的空格：

`unexpand -a {{path/to/file}}`

- 仅转换开头的空格序列（覆盖 -a 选项）：

`unexpand --first-only {{path/to/file}}`

- 将制表符设置为特定的字符间距，而不是 8（启用 -a 选项）：

`unexpand -t {{number}} {{path/to/file}}`