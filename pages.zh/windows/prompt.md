# 提示

> 更改命令窗口中的默认DOS样式提示。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/prompt>。

- 将提示重置为默认设置：

`prompt`

- 设置特定的提示：

`prompt {{prompt}}`

- 更改提示以先显示当前日期：

`prompt $D $P$G`

- 更改提示以先显示当前时间：

`prompt $T $P$G`

- 通过添加特定文本来更改提示：

`prompt {{text}} $P$G`