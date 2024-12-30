# pnmtopalm

> 将PNM图像转换为Palm位图。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmtopalm.html>。

- 将PNM图像转换为Palm位图：

`pnmtopalm {{path/to/file.pnm}} > {{path/to/file.palm}}`

- 指定生成位图的颜色深度：

`pnmtopalm -depth {{1|2|4|8|16}} {{path/to/file.pnm}} > {{path/to/file.palm}}`

- 选择生成位图的压缩方法：

`pnmtopalm -{{scanline_compression|rle_compression|packbits_compression}} {{path/to/file.pnm}} > {{path/to/file.palm}}`

- 构建自定义调色板并将其包含在生成的位图中：

`pnmtopalm -colormap {{path/to/file.pnm}} > {{path/to/file.palm}}`

- 指定位图的密度：

`pnmtopalm -density {{72|108|144|216|288}} {{path/to/file.pnm}} > {{path/to/file.palm}}`