# pnmcolormap

> 为 PNM 图像创建量化颜色映射。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmcolormap.html>.

- 生成一个使用尽可能接近输入图像的 `n_colors` 或更少颜色的图像：

`pnmcolormap {{n_colors}} {{path/to/input.pnm}} > {{path/to/output.ppm}}`

- 使用 splitspread 策略确定输出颜色，可能对细节较少的图像产生更好的结果：

`pnmcolormap -splitspread {{n_colors}} {{path/to/input.pnm}} > {{path/to/output.ppm}}`

- 对生成的颜色映射进行排序，这在比较颜色映射时非常有用：

`pnmcolormap -sort {{path/to/input.pnm}} > {{path/to/output.ppm}}`