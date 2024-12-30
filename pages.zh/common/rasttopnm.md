# rasttopnm

> 将Sun光栅文件转换为PNM文件。
> 更多信息：<https://netpbm.sourceforge.net/doc/rasttopnm.html>。

- 将RAST图像转换为PNM文件：

`rasttopnm {{path/to/input.rast}} > {{path/to/output.pnm}}`

- 如果光栅中的颜色值是颜色索引，则使用颜色表索引：

`rasttopnm -index {{path/to/input.rast}} > {{path/to/output.pnm}}`