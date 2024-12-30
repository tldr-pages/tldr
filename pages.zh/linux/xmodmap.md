# xmodmap

> 用于修改 X 中的键盘映射和指针按钮映射的工具。
> 更多信息：<https://manned.org/xmodmap>。

- 交换指针的左键单击和右键单击：

`xmodmap -e 'pointer = 3 2 1'`

- 将键盘上的一个键重新分配到另一个键：

`xmodmap -e 'keycode {{keycode}} = {{keyname}}'`

- 禁用键盘上的一个键：

`xmodmap -e 'keycode {{keycode}} ='`

- 执行指定文件中的所有 xmodmap 表达式：

`xmodmap {{path/to/file}}`