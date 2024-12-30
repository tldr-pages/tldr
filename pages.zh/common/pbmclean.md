# pbmclean

> 通过擦除孤立的黑白像素来清理 PBM 图像。
> 更多信息：<https://netpbm.sourceforge.net/doc/pbmclean.html>。

- 通过擦除孤立的黑白像素来清理 PBM 图像：

`pbmclean {{path/to/image.pbm}} > {{path/to/output.pbm}}`

- 仅清理黑色/白色像素：

`pbmclean -{{black|white}} {{path/to/image.pbm}} > {{path/to/output.pbm}}`

- 指定同一颜色的邻近像素的最小数量，以便像素不被视为孤立：

`pbmclean -minneighbours {{3}} {{path/to/image.pbm}} > {{path/to/output.pbm}}`