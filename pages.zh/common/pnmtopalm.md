# pnmtopalm

> 将 PNM 图像转换为 Palm 位图。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmtopalm.html>。

- 将 PNM 图像转换为 Palm 位图：

`pnmtopalm {{path/to/file.pnm}} > {{path/to/file.palm}}`

- 指定生成的位图的色彩深度：

`pnmtopalm -depth {{1|2|4|8|16}} {{path/to/file.pnm}} > {{path/to/file.palm}}`

- 选择生成的位图的压缩方法：

`pnmtopalm -{{scanline_compression|rle_compression|packbits_compression}} {{path/to/file.pnm}} > {{path/to/file.palm}}`

- 构建自定义颜色映射表并包含在生成的位图中：

`pnmtopalm -colormap {{path/to/file.pnm}} > {{path/to/file.palm}}`

- 指定位图的密度：

`pnmtopalm -density {{72|108|144|216|288}} {{path/to/file.pnm}} > {{path/to/file.palm}}`