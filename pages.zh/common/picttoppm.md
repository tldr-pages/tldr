# picttoppm

> 将 Macintosh PICT 文件转换为 PPM 图像。
> 更多信息：<https://netpbm.sourceforge.net/doc/picttoppm.html>。

- 将 PICT 文件转换为 PPM 图像：

`picttoppm {{path/to/file.pict}} > {{path/to/file.ppm}}`

- 强制将 PICT 文件中的任何图像以全分辨率输出：

`picttoppm -fullres {{path/to/file.pict}} > {{path/to/file.ppm}}`

- 不假设输入文件包含 PICT 头，并仅执行快速绘图操作：

`picttoppm -noheader -quickdraw {{path/to/file.pict}} > {{path/to/file.ppm}}`