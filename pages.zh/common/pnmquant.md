# pnmquant

> 将PNM图像中的颜色量化为更小的集合。
> 此命令是`pnmcolormap`和`pnmremap`的组合，并接受它们选项的并集，除了`-mapfile`。
> 另见：`pnmquantall`。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmquant.html>。

- 生成一个图像，使用不超过`n_colors`的颜色，尽可能接近输入图像：

`pnmquant {{n_colors}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`