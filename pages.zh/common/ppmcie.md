# ppmcie

> 将CIE颜色图表绘制为PPM图像。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmcie.html>。

- 使用REC709颜色系统绘制CIE颜色图表作为PPM图像：

`ppmcie > {{path/to/output.ppm}}`

- 指定要使用的颜色系统：

`ppmcie -{{cie|ebu|hdtv|ntsc|smpte}} > {{path/to/output.ppm}}`

- 指定单个光源的位置：

`ppmcie -{{red|green|blue}} {{xpos ypos}} > {{path/to/output.ppm}}`

- 不要使麦克斯韦三角形外的区域变暗：

`ppmcie -full > {{path/to/output.ppm}}`