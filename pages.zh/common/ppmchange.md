# ppmchange

> 将 PPM 图像中的一种颜色的所有像素更改为另一种颜色。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmchange.html>.

- 交换每对 `oldcolor` - `newcolor` 中的第一个颜色为第二个颜色：

`ppmchange {{oldcolor1 newcolor1 oldcolor2 newcolor2 ...}} {{path/to/input.ppm}} > {{path/to/output.ppm}}`

- 指定颜色必须相似到何种程度才能被视为相同：

`ppmchange -closeness {{百分比}} {{oldcolor1 newcolor1 oldcolor2 newcolor2 ...}} {{path/to/input.ppm}} > {{path/to/output.ppm}}`

- 将所有未在参数中指定的颜色像素替换为指定颜色：

`ppmchange -remainder {{color}} {{oldcolor1 newcolor1 oldcolor2 newcolor2 ...}} {{path/to/input.ppm}} > {{path/to/output.ppm}}`