# xmodmap

> 用于修改 X 环境中的键映射和指针按钮映射的工具。
> 更多信息：<https://manned.org/xmodmap>。

- 交换指针的 `<左键>` 和 `<右键>`：

`xmodmap -e 'pointer = 3 2 1'`

- 重新分配键盘上的某个键到另一个键：

`xmodmap -e 'keycode {{keycode}} = {{keyname}}'`

- 禁用键盘上的某个键：

`xmodmap -e 'keycode {{keycode}} ='`

- 执行指定文件中的所有 xmodmap 表达式：

`xmodmap {{path/to/file}}`
