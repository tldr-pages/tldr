# ppmglobe

> 生成适合粘贴到球体上的图像条带。
> 参见：`pnmmercator`。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmglobe.html>。

- 将图像转换为可以剪切并粘贴到球体上的条带：

`ppmglobe {{number_of_strips}} {{path/to/image.ppm}} > {{path/to/output.ppm}}`

- 使用指定颜色填充条带之间的区域：

`ppmglobe -background {{red}} {{number_of_strips}} {{path/to/image.ppm}} > {{path/to/output.ppm}}`