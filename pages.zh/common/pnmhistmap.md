# pnmhistmap

> 绘制PNM图像的直方图。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmhistmap.html>。

- 绘制PNM图像的直方图：

`pnmhistmap {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- 以点的形式绘制直方图，而不是以条形形式：

`pnmhistmap -dots {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- 指定要包含的强度值范围：

`pnmhistmap -lval {{minval}} -rval {{maxval}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`