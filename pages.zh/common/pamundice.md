# pamundice

> 将一个 Netpbm 图像网格组合成一个图像。
> 参见：`pamdice`。
> 更多信息：<https://netpbm.sourceforge.net/doc/pamundice.html>。

- 组合符合 `printf` 格式文件名表达式的图像。假设网格具有特定的大小：

`pamundice {{filename_%1d_%1a.ppm}} -across {{grid_width}} -down {{grid_height}} > {{path/to/output.ppm}}`

- 假设平铺图像在水平和垂直方向上重叠指定的数量：

`pamundice {{filename_%1d_%1a.ppm}} -across {{x_value}} -down {{y_value}} -hoverlap {{value}} -voverlap {{value}} > {{path/to/output.ppm}}`

- 通过包含每行一个文件名的文本文件指定要组合的图像：

`pamundice -listfile {{path/to/file.txt}} -across {{x_value}} -down {{y_value}} > {{path/to/output.ppm}}`
