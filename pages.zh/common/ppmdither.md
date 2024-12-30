# ppmdither

> 通过应用抖动来减少图像中的颜色数量。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmdither.html>。

- 读取 PPM 图像，应用抖动并保存到文件：

`ppmdither {{path/to/image.ppm}} > {{path/to/file.ppm}}`

- 指定每种原色的所需色调数量：

`ppmdither -red {{2}} -green {{3}} -blue {{2}} {{path/to/image.ppm}} > {{path/to/file.ppm}}`

- 指定抖动矩阵的尺寸：

`ppmdither -dim {{2}} {{path/to/image.ppm}} > {{path/to/file.ppm}}`