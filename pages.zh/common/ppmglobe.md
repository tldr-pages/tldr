# ppmglobe

> 生成适合粘贴到球体上的图像条带。
> 另见：`pnmmercator`。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmglobe.html>。

- 将图像转换为可以裁剪并粘贴到球体上的条带：

`ppmglobe {{条带数量}} {{图像路径/image.ppm}} > {{输出路径/output.ppm}}`

- 使用指定的颜色填充条带之间的区域：

`ppmglobe -background {{红色}} {{条带数量}} {{图像路径/image.ppm}} > {{输出路径/output.ppm}}`