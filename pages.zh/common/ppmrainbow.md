# ppmrainbow

> 生成一个彩虹。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmrainbow.html>。

- 生成由指定颜色组成的彩虹：

`ppmrainbow {{color1 color2 ...}} > {{path/to/output_file.ppm}}`

- 指定输出的大小（像素）：

`ppmrainbow -width {{width}} -height {{height}} {{color1 color2 ...}} > {{path/to/output_file.ppm}}`

- 用最后指定的颜色结束彩虹，不重复第一个颜色：

`ppmrainbow -norepeat {{color1 color2 ...}} > {{path/to/output_file.ppm}}`