# pbmtopgm

> 将 PBM 图像转换为 PGM，通过平均每个像素周围的 `w`x`h` 区域。
> 参见：`pnmconvol`, `pamditherbw`。
> 更多信息：<https://netpbm.sourceforge.net/doc/pbmtopgm.html>。

- 通过平均每个像素周围的 `w`x`h` 区域，将 PBM 图像转换为 PGM：

`pbmtopgm {{w}} {{h}} {{path/to/image.pbm}} > {{path/to/output.pgm}}`
