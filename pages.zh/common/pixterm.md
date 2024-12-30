# pixterm

> 在终端中打印图像。
> 另见：`chafa`，`catimg`。
> 更多信息：<https://github.com/eliukblau/pixterm>。

- 直接在终端中呈现静态图像：

`pixterm {{path/to/file}}`

- 使用图像的原始长宽比：

`pixterm -s 2 {{path/to/file}}`

- 使用特定数量的 [t]erminal [r]ows 和 [c]olumns 指定自定义长宽比：

`pixterm -tr {{24}} -tc {{80}} {{path/to/file}}`

- 使用 [m]atte 背景颜色和字符 [d]ithering 过滤输出：

`pixterm -m {{000000}} -d 2 {{path/to/file}}`