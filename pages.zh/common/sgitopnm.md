# sgitopnm

> 将SGI文件转换为PNM文件。
> 更多信息：<https://netpbm.sourceforge.net/doc/sgitopnm.html>。

- 将SGI图像转换为PNM文件：

`sgitopnm {{path/to/input.sgi}} > {{path/to/output.pnm}}`

- 显示SGI文件的信息：

`sgitopnm -verbose {{path/to/input.sgi}} > {{path/to/output.pnm}}`

- 提取SGI文件的第n个通道：

`sgitopnm -channel {{n}} {{path/to/input.sgi}} > {{path/to/output.pnm}}`