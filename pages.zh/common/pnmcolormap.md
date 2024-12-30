# pnmcolormap

> 为PNM图像创建量化颜色映射。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmcolormap.html>。

- 生成一幅使用不超过`n_colors`种颜色的图像，尽可能接近输入图像：

`pnmcolormap {{n_colors}} {{path/to/input.pnm}} > {{path/to/output.ppm}}`

- 使用splitspread策略确定输出颜色，可能会为细节较小的图像产生更好的结果：

`pnmcolormap -splitspread {{n_colors}} {{path/to/input.pnm}} > {{path/to/output.ppm}}`

- 对生成的颜色映射进行排序，这对于比较颜色映射很有用：

`pnmcolormap -sort {{path/to/input.pnm}} > {{path/to/output.ppm}}`