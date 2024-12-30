# fitstopnm

> 将灵活图像传输系统（FITS）文件转换为PNM图像。
> 另请参见：`pamtofits`。
> 更多信息：<https://netpbm.sourceforge.net/doc/fitstopnm.html>。

- 将FITS文件转换为PNM图像：

`fitstopnm {{path/to/file.fits}} > {{path/to/output.pnm}}`

- 转换FITS文件中第三个轴上指定位置的图像：

`fitstopnm -image {{z_position}} {{path/to/file.fits}} > {{path/to/output.pnm}}`