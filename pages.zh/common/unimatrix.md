# unimatrix

> 使用 Unicode 字符模拟《黑客帝国》的视觉效果。
> 请参阅：`cmatrix`。
> 更多信息：<https://github.com/will8211/unimatrix>.

- 模仿 `cmatrix` 的默认输出（无 Unicode，适用于 TTY）：

`unimatrix --no-bold --speed {{96}} --character-list {{o}}`

- 无粗体字符，缓慢地显示，使用表情符号、数字和少量符号：

`unimatrix --no-bold --speed {{50}} --character-list {{ens}}`

- 更改字符的颜色：

`unimatrix --color {{red|green|blue|white|...}}`

- 使用字母代码选择字符集（可用字符集请参阅 `unimatrix --help`）：

`unimatrix --character-list {{character_sets}}`

- 更改滚动速度：

`unimatrix --speed {{number}}`
