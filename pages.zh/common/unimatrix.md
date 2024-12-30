# unimatrix

> 使用Unicode字符模拟矩阵效果。
> 另见：`cmatrix`。
> 更多信息：<https://github.com/will8211/unimatrix>。

- 模仿`cmatrix`的默认输出（无Unicode，适用于TTY）：

`unimatrix --no-bold --speed {{96}} --character-list {{o}}`

- 无粗体字符，速度较慢，使用表情符号、数字和一些符号：

`unimatrix --no-bold --speed {{50}} --character-list {{ens}}`

- 更改字符颜色：

`unimatrix --color {{red|green|blue|white|...}}`

- 使用字母代码选择字符集（请参见`unimatrix --help`以获取可用字符集）：

`unimatrix --character-list {{character_sets}}`

- 更改滚动速度：

`unimatrix --speed {{number}}`