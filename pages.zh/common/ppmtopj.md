# ppmtopj

> 将 PPM 文件转换为 HP PaintJet 文件。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmtopj.html>。

- 将 PPM 文件转换为 HP PaintJet 文件：

`ppmtopj {{path/to/input.ppm}} > {{path/to/output.pj}}`

- 在 x 和 y 方向上移动图像：

`ppmtopj -xpos {{dx}} -ypos {{dy}} {{path/to/input.ppm}} > {{path/to/output.pj}}`

- 显式指定伽马值：

`ppmtopj -gamma {{gamma}} {{path/to/input.ppm}} > {{path/to/output.pj}}`