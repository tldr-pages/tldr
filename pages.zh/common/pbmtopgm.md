# pbmtopgm

> 通过对每个像素周围的区域进行平均，将 PBM 图像转换为 PGM。
> 另见：`pnmconvol`，`pamditherbw`。
> 更多信息：<https://netpbm.sourceforge.net/doc/pbmtopgm.html>。

- 通过对每个像素周围的 `w`x`h` 大小区域进行平均，将 PBM 图像转换为 PGM：

`pbmtopgm {{w}} {{h}} {{path/to/image.pbm}} > {{path/to/output.pgm}}`