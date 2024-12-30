# wtype

> 在Wayland上模拟键盘输入，类似于X11的`xdotool type`。
> 另见：`ydotool`。
> 更多信息：<https://github.com/atx/wtype>。

- 模拟输入文本：

`wtype "{{Hello World}}"`

- 输入特定的按键：

`wtype -k {{Left}}`

- 按下一个修饰键：

`wtype -M {{shift|ctrl|...}}`

- 释放一个修饰键：

`wtype -m {{ctrl}}`

- 在按键之间等待（以毫秒为单位）：

`wtype -d {{500}} -- "{{text}}"`

- 从`stdin`读取文本：

`echo "{{text}}" | wtype -`