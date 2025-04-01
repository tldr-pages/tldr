# pnmmercator

> 对 Netpbm 图像执行墨卡托变换。
> 参见: `pnmglobe`。
> 更多信息: <https://netpbm.sourceforge.net/doc/pnmmercator.html>。

- 将矩形投影的世界地图转换为墨卡托投影：

`pnmmercator {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- 将墨卡托投影的世界地图转换为矩形投影：

`pnmmercator -inverse {{path/to/image.pnm}} > {{path/to/output.pnm}}`
