# pbmtoepsi

> 将 PBM 图像转换为封装的 PostScript 样式预览位图。
> 更多信息：<https://netpbm.sourceforge.net/doc/pbmtoepsi.html>。

- 将 PBM 图像转换为封装的 PostScript 样式预览位图：

`pbmtoepsi {{path/to/image.pbm}} > {{path/to/output.bmp}}`

- 生成指定分辨率的正方形输出图像：

`pbmtoepsi -dpi {{144}} {{path/to/image.pbm}} > {{path/to/output.bmp}}`

- 生成具有指定水平和垂直分辨率的输出图像：

`pbmtoepsi -dpi {{72x144}} {{path/to/image.pbm}} > {{path/to/output.bmp}}`

- 仅创建边界框：

`pbmtoepsi -bbonly {{path/to/image.pbm}} > {{path/to/output.bmp}}`
