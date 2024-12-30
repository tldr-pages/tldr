# pgmramp

> 生成灰度图。
> 更多信息：<https://netpbm.sourceforge.net/doc/pgmramp.html>。

- 生成从左到右的灰度图：

`pgmtexture -lr > {{path/to/output.pgm}}`

- 生成从上到下的灰度图：

`pgmtexture -tb > {{path/to/output.pgm}}`

- 生成矩形灰度图：

`pgmtexture -rectangle > {{path/to/output.pgm}}`

- 生成椭圆形灰度图：

`pgmtexture -ellipse {{path/to/image.pgm}} > {{path/to/output.pgm}}`

- 生成从左上角到右下角的灰度图：

`pgmtexture -diagonal {{path/to/image.pgm}} > {{path/to/output.pgm}}`