# prompt

> 在命令窗口中更改默认的 DOS 风格提示。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/prompt>.

- 将提示符重置为默认设置：

`prompt`

- 设置特定的提示符：

`prompt {{prompt}}`

- 更改提示符，使其首先显示当前日期：

`prompt $D $P$G`

- 更改提示符，使其首先显示当前时间：

`prompt $T $P$G`

- 更改提示符，添加特定文本在前：

`prompt {{text}} $P$G`