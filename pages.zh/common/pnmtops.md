# pnmtops

> 将 PNM 图像转换为 PostScript 文件。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmtops.html>.

- 将 PNM 图像转换为 PS 文件：

`pnmtops {{path/to/file.pnm}} > {{path/to/file.ps}}`

- 指定输出图像的尺寸（以英寸为单位）：

`pnmtops -imagewidth {{imagewidth}} -imageheight {{imageheight}} {{path/to/file.pnm}} > {{path/to/file.ps}}`

- 指定输出图像所在页面的尺寸（以英寸为单位）：

`pnmtops -width {{width}} -height {{height}} {{path/to/file.pnm}} > {{path/to/file.ps}}`
