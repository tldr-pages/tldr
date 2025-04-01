# pnmhistmap

> 绘制 PNM 图像的直方图。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmhistmap.html>.

- 绘制 PNM 图像的直方图：

`pnmhistmap {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- 用点而不是条形绘制直方图：

`pnmhistmap -dots {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- 指定要包含的强度值范围：

`pnmhistmap -lval {{minval}} -rval {{maxval}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`