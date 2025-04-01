# fitstopnm

> 将 Flexible Image Transport System (FITS) 文件转换为 PNM 图像。
> 参见：`pamtofits`。
> 更多信息：<https://netpbm.sourceforge.net/doc/fitstopnm.html>。

- 将 FITS 文件转换为 PNM 图像：

`fitstopnm {{path/to/file.fits}} > {{path/to/output.pnm}}`

- 将 FITS 文件中第三轴指定位置的图像转换为 PNM 图像：

`fitstopnm -image {{z_position}} {{path/to/file.fits}} > {{path/to/output.pnm}}`