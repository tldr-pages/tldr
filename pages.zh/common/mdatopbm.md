# mdatopbm

> 将 Microdesign MDA 文件转换为 PBM 图像。
> 参见: `pbmtomda`。
> 更多信息: <https://netpbm.sourceforge.net/doc/mdatopbm.html>。

- 将 MDA 文件转换为 PBM 图像：

`mdatopbm {{path/to/image.mda}} > {{path/to/output.pbm}}`

- 反转输入图像的颜色：

`mdatopbm -i {{path/to/image.mda}} > {{path/to/output.pbm}}`

- 将输入图像的高度加倍：

`mdatopbm -d {{path/to/image.mda}} > {{path/to/output.pbm}}`
