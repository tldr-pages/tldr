# pastel

> 生成、分析、转换和操作颜色。
> 更多信息：<https://github.com/sharkdp/pastel>。

- 将颜色从一种格式转换为另一种格式。这里是从 RGB 转换为 HSL：

`pastel format {{hsl}} {{ff8000}}`

- 在终端上显示和分析颜色：

`pastel color "{{rgb(255,50,127)}}"`

- 从屏幕上的某个位置选择颜色：

`pastel pick`

- 生成一组 N 个视觉上不同的颜色：

`pastel distinct {{8}}`

- 列出所有 X11/CSS 颜色名称：

`pastel list`
