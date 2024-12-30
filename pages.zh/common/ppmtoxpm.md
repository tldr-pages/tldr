# ppmtoxpm

> 将PPM图像转换为X11版本3的位图。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmtoxpm.html>。

- 将PPM图像转换为XPM图像：

`ppmtoxpm {{path/to/input_file.ppm}} > {{path/to/output_file.xpm}}`

- 在输出的XPM图像中指定前缀字符串：

`ppmtoxpm -name {{prefix_string}} {{path/to/input_file.ppm}} > {{path/to/output_file.xpm}}`

- 在输出的XPM文件中，通过十六进制代码指定颜色，而不是通过名称：

`ppmtoxpm -hexonly {{path/to/input_file.ppm}} > {{path/to/output_file.xpm}}`

- 使用指定的PGM文件作为透明度遮罩：

`ppmtoxpm -alphamask {{path/to/alpha_file.pgm}} {{path/to/input_file.ppm}} > {{path/to/output_file.xpm}}`