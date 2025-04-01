# pnmsmooth

> 平滑 PNM 图像。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmsmooth.html>.

- 使用 3x3 的卷积矩阵平滑 PNM 图像：

`pnmsmooth {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- 使用指定宽度和高度的卷积矩阵平滑 PNM 图像：

`pnmsmooth -width {{width}} -height {{height}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`