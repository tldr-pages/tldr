# xsel

> X11 选择和剪贴板操作工具。
> 更多信息：<https://manned.org/xsel>。

- 将命令的输出作为剪贴板的输入（相当于 `Ctrl + C`）：

`echo 123 | xsel -ib`

- 使用文件的内容作为剪贴板的输入：

`cat {{path/to/file}} | xsel -ib`

- 将剪贴板的内容输出到终端（相当于 `Ctrl + V`）：

`xsel -ob`

- 将剪贴板的内容输出到文件：

`xsel -ob > {{path/to/file}}`

- 清空剪贴板：

`xsel -cb`

- 将 X11 主选择的内容输出到终端（相当于鼠标中键点击）：

`xsel -op`