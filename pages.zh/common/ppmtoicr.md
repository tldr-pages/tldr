# ppmtoicr

> 将PPM图像转换为NCSA ICR格式。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmtoicr.html>。

- 将PPM图像转换为ICR文件：

`ppmtoicr {{path/to/file.ppm}} > {{path/to/file.icr}}`

- 在指定名称的窗口中显示输出：

`ppmtoicr -windowname {{name}} {{path/to/file.ppm}} > {{path/to/file.icr}}`

- 按指定因子扩大图像：

`ppmtoicr -expand {{factor}} {{path/to/file.ppm}} > {{path/to/file.icr}}`

- 在屏幕上显示输出，指定编号：

`ppmtoicr -display {{number}} {{path/to/file.ppm}} > {{path/to/file.icr}}`