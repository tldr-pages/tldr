# ppmpat

> 生成带图案的 PPM 图像。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmpat.html>.

- 生成指定图案和尺寸的 PPM 文件：

`ppmpat -{{gingham2|gingham3|madras|tartan|poles|...}} {{width}} {{height}} > {{path/to/file.ppm}}`

- 使用指定的颜色生成迷彩图案的 PPM 文件：

`ppmpat -camo -color {{color1,color2,...}} {{width}} {{height}} > {{path/to/file.ppm}}`
