# pamdice

> 垂直或水平切片 Netpbm 图像。
> 另请参见：`pamundice`。
> 更多信息：<https://netpbm.sourceforge.net/doc/pamdice.html>。

- 切片一个 Netpbm 图像，使得生成的图块具有指定的高度和宽度：

`pamdice -outstem {{path/to/filename_stem}} -height {{value}} -width {{value}} {{path/to/input.ppm}}`

- 使生成的部分在水平方向和垂直方向上重叠指定的量：

`pamdice -outstem {{path/to/filename_stem}} -height {{value}} -width {{value}} -hoverlap {{value}} -voverlap {{value}} {{path/to/input.ppm}}`