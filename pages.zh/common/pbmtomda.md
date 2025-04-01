# pbmtomda

> 将 PBM 图像转换为 Microdesign MDA 文件。
> 参见：`mdatopbm`。
> 更多信息：<https://netpbm.sourceforge.net/doc/pbmtomda.html>。

- 将 PBM 图像转换为 MDA 文件：

`pbmtomda {{path/to/image.pbm}} > {{path/to/output.mda}}`

- 反转输入图像的颜色：

`pbmtomda -i {{path/to/image.pbm}} > {{path/to/output.mda}}`

- 将输入图像的高度减半：

`pbmtomda -d {{path/to/image.pbm}} > {{path/to/output.mda}}`