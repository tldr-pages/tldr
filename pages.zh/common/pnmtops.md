# pnmtops

> 将PNM图像转换为PostScript文件。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmtops.html>。

- 将PNM图像转换为PS文件：

`pnmtops {{path/to/file.pnm}} > {{path/to/file.ps}}`

- 指定输出图像的尺寸（以英寸为单位）：

`pnmtops -imagewidth {{imagewidth}} -imageheight {{imageheight}} {{path/to/file.pnm}} > {{path/to/file.ps}}`

- 指定输出图像所在页面的尺寸（以英寸为单位）：

`pnmtops -width {{width}} -height {{height}} {{path/to/file.pnm}} > {{path/to/file.ps}}`