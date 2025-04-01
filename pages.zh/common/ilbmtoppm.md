# ilbmtoppm

> 将 ILBM 文件转换为 PPM 图像。
> 更多信息：<https://netpbm.sourceforge.net/doc/ilbmtoppm.html>。

- 将 ILBM 文件转换为 PPM 图像：

`ilbmtoppm {{path/to/file.ilbm}} > {{path/to/file.ppm}}`

- 使用指定的颜色在图像透明的地方“显示”：

`ilbmtoppm -transparent {{color}} {{path/to/file.ilbm}} > {{path/to/file.ppm}}`

- 忽略具有指定块 ID 的块：

`ilbmtoppm -ignore {{chunkID}} {{path/to/file.ilbm}} > {{path/to/file.ppm}}`

- 将输入的透明度信息存储到指定的 PBM 文件中：

`ilbmtoppm -maskfile {{path/to/maskfile.pbm}} {{path/to/file.ilbm}} > {{path/to/file.ppm}}`
