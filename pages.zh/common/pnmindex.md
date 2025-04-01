# pnmindex

> 构建多个 PNM 图像的视觉索引。
> 参见：`pamundice`。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmindex.html>。

- 生成一个包含指定图像的缩略图的网格图像：

`pnmindex {{path/to/input1.pnm path/to/input2.pnm ...}} > {{path/to/output.pnm}}`

- 指定（正方形）缩略图的大小：

`pnmindex -size {{50}} {{path/to/input1.pnm path/to/input2.pnm ...}} > {{path/to/output.pnm}}`

- 指定每行的缩略图数量：

`pnmindex -across {{10}} {{path/to/input1.pnm path/to/input2.pnm ...}} > {{path/to/output.pnm}}`

- 指定输出图像的最大颜色数：

`pnmindex -colors {{512}} {{path/to/input1.pnm path/to/input2.pnm ...}} > {{path/to/output.pnm}}`
