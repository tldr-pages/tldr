# xpmtoppm

> 将 X11 图像文件转换为 PPM 图像。
> 更多信息：<https://netpbm.sourceforge.net/doc/xpmtoppm.html>。

- 将 XPM 图像文件转换为 PPM 图像文件：

`xpmtoppm {{path/to/input_file.xpm}} > {{path/to/output_file.ppm}}`

- 将输入图像的透明度掩码保存到指定文件中：

`xpmtoppm --alphaout {{path/to/alpha_file.pbm}} {{path/to/input_file.xpm}} > {{path/to/output_file.ppm}}`
