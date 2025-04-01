# sgitopnm

> 将 SGI 文件转换为 PNM 文件。
> 更多信息：<https://netpbm.sourceforge.net/doc/sgitopnm.html>。

- 将 SGI 图像转换为 PNM 文件：

`sgitopnm {{path/to/input.sgi}} > {{path/to/output.pnm}}`

- 显示 SGI 文件的信息：

`sgitopnm -verbose {{path/to/input.sgi}} > {{path/to/output.pnm}}`

- 提取 SGI 文件的第 n 个通道：

`sgitopnm -channel {{n}} {{path/to/input.sgi}} > {{path/to/output.pnm}}`