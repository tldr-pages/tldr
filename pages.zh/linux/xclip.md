# xclip

> X11 剪贴板操作工具，类似于 `xsel`。
> 处理 X11 主选择区和次选择区，以及系统剪贴板（`<Ctrl c>`/`<Ctrl v>`）。
> 另请参见：`wl-copy`。
> 更多信息：<https://manned.org/xclip>。

- 将命令的输出复制到 X11 主选择区（剪贴板）：

`echo 123 | xclip`

- 将命令的输出复制到指定的 X11 选择区：

`echo 123 | xclip -selection {{primary|secondary|clipboard}}`

- 使用简短标记将命令的输出复制到系统剪贴板：

`echo 123 | xclip -sel clip`

- 将文件内容复制到系统剪贴板：

`xclip -sel clip {{input_file.txt}}`

- 将 PNG 图片内容复制到系统剪贴板（可在其他程序中正确粘贴）：

`xclip -sel clip -t image/png {{input_file.png}}`

- 将控制台中的用户输入复制到系统剪贴板：

`xclip -i`

- 将 X11 主选择区的内容粘贴到控制台：

`xclip -o`

- 将系统剪贴板的内容粘贴到控制台：

`xclip -o -sel clip`
