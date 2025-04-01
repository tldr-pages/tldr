# ppmdist

> 生成 PPM 图像的灰度版本。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmdist.html>。

- 生成指定 PPM 图像的灰度版本：

`ppmdist {{path/to/input.ppm}} > {{path/to/output.pgm}}`

- 使用指定的方法将颜色映射为灰度值：

`ppmdist -{{frequency|intensity}} {{path/to/input.ppm}} > {{path/to/output.pgm}}`