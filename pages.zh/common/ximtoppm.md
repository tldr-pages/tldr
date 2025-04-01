# ximtoppm

> 将 XIM 文件转换为 PPM 图像。
> 更多信息：<https://netpbm.sourceforge.net/doc/ximtoppm.html>.

- 将 XIM 图像转换为 PPM 图像：

`ximtoppm {{path/to/input_file.xim}} > {{path/to/output_file.ppm}}`

- 将输入图像的透明度掩码存储在指定文件中：

`ximtoppm --alphaout {{path/to/alpha_file.pbm}} {{path/to/input_file.xim}} > {{path/to/output_file.ppm}}`