# ppmtv

> 让 PPM 图像看起来像是从美国电视上拍摄的。
> 按指定的调暗因子（0 到 1 之间的数字）将图像数据的每隔一行调暗。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmtv.html>。

- 赋予 PPM 图像美国电视的外观：

`ppmtv {{dim_factor}} {{path/to/file.ppm}} > {{path/to/output.ppm}}`

- 抑制所有信息消息：

`ppmtv -quiet`

- 显示版本：

`ppmtv -version`