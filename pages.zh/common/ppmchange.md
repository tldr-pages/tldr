# ppmchange

> 将PPM图像中一种颜色的所有像素更改为另一种颜色。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmchange.html>。

- 用第二种颜色交换每对`旧颜色` - `新颜色`中的第一种颜色：

`ppmchange {{oldcolor1 newcolor1 oldcolor2 newcolor2 ...}} {{path/to/input.ppm}} > {{path/to/output.ppm}}`

- 指定颜色相似度的要求，以便被视为相同：

`ppmchange -closeness {{percentage}} {{oldcolor1 newcolor1 oldcolor2 newcolor2 ...}} {{path/to/input.ppm}} > {{path/to/output.ppm}}`

- 用一种颜色替换未在参数中指定的所有像素：

`ppmchange -remainder {{color}} {{oldcolor1 newcolor1 oldcolor2 newcolor2 ...}} {{path/to/input.ppm}} > {{path/to/output.ppm}}`