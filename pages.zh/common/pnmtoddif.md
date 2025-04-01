# pnmtoddif

> 将 PNM 图像转换为 DDIF 图像文件。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmtoddif.html>.

- 将 PNM 图像转换为 DDIF 图像文件：

`pnmtoddif {{path/to/image.pnm}} > {{path/to/image.ddif}}`

- 明确指定输出图像的水平和垂直分辨率：

`pnmtoddif -resolution {{horizontal_dpi}} {{vertical_dpi}} {{path/to/image.pnm}} > {{path/to/image.ddif}}`
