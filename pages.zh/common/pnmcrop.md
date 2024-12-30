# pnmcrop

> 裁剪 PNM 图像。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmcrop.html>。

- 移除 PNM 图像的白色边框：

`pnmcrop -white {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- 移除图像顶部和左侧指定颜色的边框：

`pnmcrop -bg-color {{color}} -top -left {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- 通过指定角落的像素颜色来确定要移除的边框颜色：

`pnmcrop -bg-corner {{topleft|topright|bottomleft|bottomright}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- 留下宽度为 `n` 像素的边框。此外，指定如果图像完全由背景构成时的行为：

`pnmcrop -margins {{n}} -blank-image {{pass|minimize|maxcrop}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`