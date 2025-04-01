# xsel

> X11 选择和剪贴板操作工具。
> 更多信息：<https://manned.org/xsel>。

- 将命令的输出作为剪贴板的输入（相当于 `<Ctrl c>`）：

`echo 123 | xsel {{[-ib|--input --clipboard]}}`

- 将文件的内容作为剪贴板的输入：

`cat {{path/to/file}} | xsel {{[-ib|--input --clipboard]}}`

- 将剪贴板的内容输出到终端（相当于 `<Ctrl v>`）：

`xsel {{[-ob|--output --clipboard]}}`

- 将剪贴板的内容输出到文件：

`xsel {{[-ob|--output --clipboard]}} > {{path/to/file}}`

- 清除剪贴板：

`xsel {{[-cb|--clear --clipboard]}}`

- 将 X11 主选区的内容输出到终端（相当于鼠标 `<MiddleClick>`）：

`xsel {{[-op|--output --primary]}}`