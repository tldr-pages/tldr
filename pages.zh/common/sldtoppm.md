# sldtoppm

> 将 AutoCAD 滑动文件转换为 PPM 图像。
> 更多信息：<https://netpbm.sourceforge.net/doc/sldtoppm.html>.

- 将 SLD 文件转换为 PPM 图像：

`sldtoppm {{path/to/input.sld}} > {{path/to/output.ppm}}`

- 通过调整图像的宽度来补偿非方形像素：

`sldtoppm -adjust {{path/to/input.sld}} > {{path/to/output.ppm}}`