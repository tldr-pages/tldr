# rasttopnm

> 将 Sun 光栅文件转换为 PNM 文件。
> 更多信息：<https://netpbm.sourceforge.net/doc/rasttopnm.html>。

- 将 RAST 图像转换为 PNM 文件：

`rasttopnm {{path/to/input.rast}} > {{path/to/output.pnm}}`

- 如果光栅中的颜色值为颜色索引，则使用这些索引：

`rasttopnm -index {{path/to/input.rast}} > {{path/to/output.pnm}}`
