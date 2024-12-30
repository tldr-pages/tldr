# jpegtran

> 执行无损JPEG文件转换。
> 更多信息：<https://manned.org/jpegtran>。

- 水平或垂直翻转图像：

`jpegtran -flip {{horizontal|vertical}} {{path/to/image.jpg}} > {{path/to/output.jpg}}`

- 将图像顺时针旋转90、180或270度：

`jpegtran -rotate {{90|180|270}} {{path/to/image.jpg}} > {{path/to/output.jpg}}`

- 沿左上到右下轴转置图像：

`jpegtran -transpose {{path/to/image.jpg}} > {{path/to/output.jpg}}`

- 沿右上到左下轴转置图像：

`jpegtran -transverse {{path/to/image.jpg}} > {{path/to/output.jpg}}`

- 将图像转换为灰度：

`jpegtran -grayscale {{path/to/image.jpg}} > {{path/to/output.jpg}}`

- 将图像裁剪为从左上角开始的宽度为 `W` 和高度为 `H` 的矩形区域，并将输出保存到特定文件：

`jpegtran -crop {{W}}x{{H}} -outfile {{path/to/output.jpg}} {{path/to/image.jpg}}`

- 将图像裁剪为宽度为 `W` 和高度为 `H` 的矩形区域，从左上角的点 `X` 和 `Y` 开始：

`jpegtran -crop {{W}}x{{H}}+{{X}}+{{Y}} {{path/to/image.jpg}} > {{path/to/output.jpg}}`