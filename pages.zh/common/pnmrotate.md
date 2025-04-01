# pnmrotate

> 旋转 PNM 图像。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmrotate.html>.

- 旋转 PNM 图像（以度为单位，逆时针方向）：

`pnmrotate {{angle}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- 指定旋转输入图像后显露的背景颜色：

`pnmrotate -background {{color}} {{angle}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- 禁用抗锯齿，提高性能但降低质量：

`pnmrotate -noantialias {{angle}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`