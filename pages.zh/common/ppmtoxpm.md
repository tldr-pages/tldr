# ppmtoxpm

> 将 PPM 图像转换为 X11 版本 3 像素图。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmtoxpm.html>.

- 将 PPM 图像转换为 XPM 图像：

`ppmtoxpm {{path/to/input_file.ppm}} > {{path/to/output_file.xpm}}`

- 指定输出 XPM 图像中的前缀字符串：

`ppmtoxpm -name {{prefix_string}} {{path/to/input_file.ppm}} > {{path/to/output_file.xpm}}`

- 在输出的 XPM 文件中，使用十六进制代码而不是颜色名称指定颜色：

`ppmtoxpm -hexonly {{path/to/input_file.ppm}} > {{path/to/output_file.xpm}}`

- 使用指定的 PGM 文件作为透明度蒙版：

`ppmtoxpm -alphamask {{path/to/alpha_file.pgm}} {{path/to/input_file.ppm}} > {{path/to/output_file.xpm}}`
