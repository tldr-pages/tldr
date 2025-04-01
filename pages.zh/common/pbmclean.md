# pbmclean

> 清理 PBM 图像，通过删除孤立的黑白像素。
> 更多信息：<https://netpbm.sourceforge.net/doc/pbmclean.html>。

- 清理 PBM 图像，删除孤立的黑白像素：

`pbmclean {{path/to/image.pbm}} > {{path/to/output.pbm}}`

- 仅清理黑白像素：

`pbmclean -{{black|white}} {{path/to/image.pbm}} > {{path/to/output.pbm}}`

- 指定相同颜色的相邻像素的最小数量，以避免将某像素视为孤立：

`pbmclean -minneighbours {{3}} {{path/to/image.pbm}} > {{path/to/output.pbm}}`
