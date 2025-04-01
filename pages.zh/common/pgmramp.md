# pgmramp

> 生成灰度图。
> 更多信息：<https://netpbm.sourceforge.net/doc/pgmramp.html>。

- 从左到右生成灰度图：

`pgmramp -lr > {{path/to/output.pgm}}`

- 从上到下生成灰度图：

`pgmramp -tb > {{path/to/output.pgm}}`

- 生成矩形灰度图：

`pgmramp -rectangle > {{path/to/output.pgm}}`

- 生成椭圆形灰度图：

`pgmramp -ellipse {{path/to/image.pgm}} > {{path/to/output.pgm}}`

- 从左上角到右下角生成灰度图：

`pgmramp -diagonal {{path/to/image.pgm}} > {{path/to/output.pgm}}`