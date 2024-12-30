# xclip

> X11 剪贴板操作工具，类似于 `xsel`。
> 处理 X 的主要和次要选择，以及系统剪贴板（`Ctrl + C`/`Ctrl + V`）。
> 另见：`wl-copy`。
> 更多信息：<https://manned.org/xclip>。

- 将命令的输出复制到 X11 的主要选择区域（剪贴板）：

`echo 123 | xclip`

- 将命令的输出复制到指定的 X11 选择区域：

`echo 123 | xclip -selection {{primary|secondary|clipboard}}`

- 使用简短的表示法将命令的输出复制到系统剪贴板：

`echo 123 | xclip -sel clip`

- 将文件的内容复制到系统剪贴板：

`xclip -sel clip {{input_file.txt}}`

- 将 PNG 的内容复制到系统剪贴板（可以在其他程序中正确粘贴）：

`xclip -sel clip -t image/png {{input_file.png}}`

- 将控制台中的用户输入复制到系统剪贴板：

`xclip -i`

- 将 X11 主要选择区域的内容粘贴到控制台：

`xclip -o`

- 将系统剪贴板的内容粘贴到控制台：

`xclip -o -sel clip`