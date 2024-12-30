# pnmrotate

> 旋转 PNM 图像。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmrotate.html>。

- 按一定角度（以度数为单位，逆时针方向）旋转 PNM 图像：

`pnmrotate {{angle}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- 指定旋转输入图像时暴露的背景颜色：

`pnmrotate -background {{color}} {{angle}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- 禁用抗锯齿，提升性能但降低质量：

`pnmrotate -noantialias {{angle}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`