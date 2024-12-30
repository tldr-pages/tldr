# pamundice

> 将一组 Netpbm 图像组合成一幅图像。
> 另见：`pamdice`。
> 更多信息：<https://netpbm.sourceforge.net/doc/pamundice.html>。

- 合并名称与 `printf` 风格文件名表达式匹配的图像。假设网格具有特定大小：

`pamundice {{filename_%1d_%1a.ppm}} -across {{grid_width}} -down {{grid_height}} > {{path/to/output.ppm}}`

- 假设瓷砖在水平和垂直方向上按指定的数量重叠：

`pamundice {{filename_%1d_%1a.ppm}} -across {{x_value}} -down {{y_value}} -hoverlap {{value}} -voverlap {{value}} > {{path/to/output.ppm}}`

- 通过包含每行一个文件名的文本文件指定要合并的图像：

`pamundice -listfile {{path/to/file.txt}} -across {{x_value}} -down {{y_value}} > {{path/to/output.ppm}}`