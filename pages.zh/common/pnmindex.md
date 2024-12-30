# pnmindex

> 构建多个 PNM 图像的视觉索引。
> 另见：`pamundice`。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmindex.html>。

- 生成一个包含指定图像缩略图的网格图像：

`pnmindex {{path/to/input1.pnm path/to/input2.pnm ...}} > {{path/to/output.pnm}}`

- 指定缩略图的大小（正方形）：

`pnmindex -size {{50}} {{path/to/input1.pnm path/to/input2.pnm ...}} > {{path/to/output.pnm}}`

- 指定每行的缩略图数量：

`pnmindex -across {{10}} {{path/to/input1.pnm path/to/input2.pnm ...}} > {{path/to/output.pnm}}`

- 指定输出中最大颜色数量：

`pnmindex -colors {{512}} {{path/to/input1.pnm path/to/input2.pnm ...}} > {{path/to/output.pnm}}`