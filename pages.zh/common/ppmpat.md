# ppmpat

> 生成一个带有图案的 PPM 图像。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmpat.html>。

- 根据指定的图案和尺寸生成一个 PPM 文件：

`ppmpat -{{gingham2|gingham3|madras|tartan|poles|...}} {{宽度}} {{高度}} > {{路径/到/文件.ppm}}`

- 使用指定颜色生成一个迷彩图案的 PPM 文件：

`ppmpat -camo -color {{颜色1,颜色2,...}} {{宽度}} {{高度}} > {{路径/到/文件.ppm}}`