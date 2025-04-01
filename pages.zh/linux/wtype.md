# wtype

> 在 Wayland 上模拟键盘输入，类似于 X11 的 `xdotool type`。
> 参见：`ydotool`。
> 更多信息：<https://github.com/atx/wtype>。

- 模拟输入文本：

`wtype "{{Hello World}}"`

- 输入特定的键：

`wtype -k {{Left}}`

- 按下修饰键：

`wtype -M {{shift|ctrl|...}}`

- 释放修饰键：

`wtype -m {{ctrl}}`

- 在按键之间等待（以毫秒为单位）：

`wtype -d {{500}} -- "{{text}}"`

- 从 `stdin` 读取文本：

`echo "{{text}}" | wtype -`