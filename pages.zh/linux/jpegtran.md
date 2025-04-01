# jpegtran

> 对 JPEG 文件进行无损转换。
> 更多信息：<https://manned.org/jpegtran>。

- 水平或垂直镜像图片：

`jpegtran -flip {{horizontal|vertical}} {{path/to/image.jpg}} > {{path/to/output.jpg}}`

- 将图片顺时针旋转 90、180 或 270 度：

`jpegtran -rotate {{90|180|270}} {{path/to/image.jpg}} > {{path/to/output.jpg}}`

- 沿左上到右下对角线转置图片：

`jpegtran -transpose {{path/to/image.jpg}} > {{path/to/output.jpg}}`

- 沿右上到左下对角线转置图片：

`jpegtran -transverse {{path/to/image.jpg}} > {{path/to/output.jpg}}`

- 将图片转换为灰度图：

`jpegtran -grayscale {{path/to/image.jpg}} > {{path/to/output.jpg}}`

- 从左上角裁剪宽度为 `W`、高度为 `H` 的矩形区域，并将输出保存到指定文件：

`jpegtran -crop {{W}}x{{H}} -outfile {{path/to/output.jpg}} {{path/to/image.jpg}}`

- 从左上角起始点 `X` 和 `Y` 裁剪宽度为 `W`、高度为 `H` 的矩形区域：

`jpegtran -crop {{W}}x{{H}}+{{X}}+{{Y}} {{path/to/image.jpg}} > {{path/to/output.jpg}}`