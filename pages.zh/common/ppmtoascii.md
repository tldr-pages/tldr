# ppmtoascii

> 将 PPM 图像转换为使用 ANSI 终端颜色代码的 ASCII 图像。
> 参见：`ppmtoterm`，`pbmtoascii`，`pbmto4425`。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmtoascii.html>。

- 将 PPM 图像转换为 ASCII 图像，将 1x2 像素区域组合成一个字符：

`ppmtoascii {{path/to/input.ppm}} > {{path/to/output.txt}}`

- 将 PPM 图像转换为 ASCII 图像，将 2x4 像素区域组合成一个字符：

`ppmtoascii -2x4 {{path/to/input.ppm}} > {{path/to/output.txt}}`
