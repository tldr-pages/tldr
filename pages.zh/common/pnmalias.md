# pnmalias

> 对PNM图像应用抗锯齿。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmalias.html>。

- 对PNM图像执行抗锯齿，将黑色像素视为背景，白色像素视为前景：

`pnmalias {{path/to/input.pnm}} > {{path/to/output.ppm}}`

- 明确指定背景色和前景色：

`pnmalias -bcolor {{背景颜色}} -fcolor {{前景颜色}} {{path/to/input.pnm}} > {{path/to/output.ppm}}`

- 仅对前景像素应用抗锯齿：

`pnmalias -fonly {{path/to/input.pnm}} > {{path/to/output.ppm}}`

- 对背景像素周围的所有像素应用抗锯齿：

`pnmalias -balias {{path/to/input.pnm}} > {{path/to/output.ppm}}`