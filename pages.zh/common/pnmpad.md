# pnmpad

> 为 PNM 图像添加边框。
> 另见：`pnmmargin`、`pamcut`、`pamcomp`。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmpad.html>。

- 向图像添加指定大小的边框：

`pnmpad -left {{100}} -right {{150}} -top {{123}} -bottom {{456}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- 将图像填充到指定大小：

`pnmpad -width {{1000}} -height {{500}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- 将图像的宽度填充到指定大小，控制左右填充的比例：

`pnmpad -width {{1000}} -halign {{0.7}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- 使用指定颜色填充图像的宽度：

`pnmpad -width {{1000}} -color {{red}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`