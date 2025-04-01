# pnmquant

> 将 PNM 图像中的颜色量化为较小的集合。
> 此命令是 `pnmcolormap` 和 `pnmremap` 的组合，接受这两个命令的选项集合，但不包括 `-mapfile`。
> 参见：`pnmquantall`。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmquant.html>。

- 生成一个使用尽可能接近输入图像的 `n_colors` 或更少颜色的图像：

`pnmquant {{n_colors}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`
