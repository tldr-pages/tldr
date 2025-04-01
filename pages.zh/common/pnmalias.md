# pnmalias

> 对 PNM 图像进行抗锯齿处理。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmalias.html>。

- 对 PNM 图像进行抗锯齿处理，将黑色像素视为背景，白色像素视为前景：

`pnmalias {{path/to/input.pnm}} > {{path/to/output.ppm}}`

- 明确指定背景和前景颜色：

`pnmalias -bcolor {{background_color}} -fcolor {{foreground_color}} {{path/to/input.pnm}} > {{path/to/output.ppm}}`

- 仅对前景像素进行抗锯齿处理：

`pnmalias -fonly {{path/to/input.pnm}} > {{path/to/output.ppm}}`

- 对背景像素周围的所有像素进行抗锯齿处理：

`pnmalias -balias {{path/to/input.pnm}} > {{path/to/output.ppm}}`