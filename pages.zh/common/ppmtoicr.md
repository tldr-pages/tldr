# ppmtoicr

> 将 PPM 图像转换为 NCSA ICR 格式。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmtoicr.html>.

- 将 PPM 图像转换为 ICR 文件：

`ppmtoicr {{path/to/file.ppm}} > {{path/to/file.icr}}`

- 以指定名称显示输出：

`ppmtoicr -windowname {{name}} {{path/to/file.ppm}} > {{path/to/file.icr}}`

- 按指定因子扩展图像：

`ppmtoicr -expand {{factor}} {{path/to/file.ppm}} > {{path/to/file.icr}}`

- 以指定编号在屏幕上显示输出：

`ppmtoicr -display {{number}} {{path/to/file.ppm}} > {{path/to/file.icr}}`