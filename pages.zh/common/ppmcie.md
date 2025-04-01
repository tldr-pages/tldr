# ppmcie

> 绘制 CIE 色度图作为 PPM 图像。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmcie.html>。

- 使用 REC709 色彩系统绘制 CIE 色度图作为 PPM 图像：

`ppmcie > {{path/to/output.ppm}}`

- 指定使用的色彩系统：

`ppmcie -{{cie|ebu|hdtv|ntsc|smpte}} > {{path/to/output.ppm}}`

- 指定各光源的位置：

`ppmcie -{{red|green|blue}} {{xpos ypos}} > {{path/to/output.ppm}}`

- 不减少 Maxwell 三角形外区域的亮度：

`ppmcie -full > {{path/to/output.ppm}}`