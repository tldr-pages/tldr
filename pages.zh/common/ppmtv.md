# ppmtv

> 使 PPM 图像看起来像是从美国电视中截取的。
> 按指定的暗化因子（0 到 1 之间的一个数字）将图像数据的每一行交替暗化。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmtv.html>。

- 给 PPM 图像添加美国电视效果：

`ppmtv {{dim_factor}} {{path/to/file.ppm}} > {{path/to/output.ppm}}`

- 抑制所有信息性消息：

`ppmtv -quiet`

- 显示版本：

`ppmtv -version`
