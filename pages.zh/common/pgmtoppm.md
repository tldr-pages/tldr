# pgmtoppm

> 为 PGM 图像上色。
> 更多信息：<https://netpbm.sourceforge.net/doc/pgmtoppm.html>.

- 将输入图像的所有灰度值映射到两个指定颜色之间的所有颜色：

`pgmtoppm -black {{red}} --white {{blue}} {{path/to/input.pgm}} > {{path/to/output.ppm}}`

- 根据指定的调色板将输入图像的所有灰度值映射到颜色：

`pgmtoppm -map {{path/to/colormap.ppm}} {{path/to/input.pgm}} > {{path/to/output.ppm}}`