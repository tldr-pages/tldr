# pamdice

> 将 Netpbm 图像垂直或水平切片。
> 参见: `pamundice`。
> 更多信息: <https://netpbm.sourceforge.net/doc/pamdice.html>。

- 将 Netpbm 图像切片，使得结果的图块具有指定的高度和宽度：

`pamdice -outstem {{path/to/filename_stem}} -height {{value}} -width {{value}} {{path/to/input.ppm}}`

- 使生成的切片在水平和垂直方向上重叠指定的距离：

`pamdice -outstem {{path/to/filename_stem}} -height {{value}} -width {{value}} -hoverlap {{value}} -voverlap {{value}} {{path/to/input.ppm}}`
