# pnmtorle

> 将PNM文件转换为犹他光栅工具RLE图像文件。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmtorle.html>。

- 将PNM图像转换为RLE图像：

`pnmtorle {{path/to/input.pnm}} > {{path/to/output.rle}}`

- 将PNM头信息打印到`stdout`：

`pnmtorle -verbose {{path/to/input.pnm}} > {{path/to/output.rle}}`

- 在输出图像中包含透明通道，其中每个黑色像素被设置为完全透明，其他每个像素被设置为完全不透明：

`pnmtorle -alpha {{path/to/input.pnm}} > {{path/to/output.rle}}`