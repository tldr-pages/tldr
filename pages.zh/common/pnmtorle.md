# pnmtorle

> 将 PNM 文件转换为 Utah Raster Tools RLE 图像文件。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmtorle.html>.

- 将 PNM 图像转换为 RLE 图像：

`pnmtorle {{path/to/input.pnm}} > {{path/to/output.rle}}`

- 将 PNM 文件头信息打印到 `stdout`：

`pnmtorle -verbose {{path/to/input.pnm}} > {{path/to/output.rle}}`

- 在输出图像中包含一个透明通道，其中每个黑色像素设为完全透明，其他像素设为完全不透明：

`pnmtorle -alpha {{path/to/input.pnm}} > {{path/to/output.rle}}`
