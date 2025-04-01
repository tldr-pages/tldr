# rawtoppm

> 将原始的 RGB 流转换为 PPM 图像。
> 更多信息：<https://netpbm.sourceforge.net/doc/rawtoppm.html>。

- 将原始的 RGB 流转换为 PPM 图像：

`rawtoppm {{width}} {{height}} {{path/to/image.raw}} > {{path/to/output.ppm}}`

- 将像素顺序为从底部开始而不是从顶部开始的原始 RGB 流转换为 PPM 图像：

`rawtoppm {{width}} {{height}} {{path/to/image.raw}} | pamflip -tb > {{path/to/output.ppm}}`

- 忽略指定文件的前 n 个字节：

`rawtoppm {{width}} {{height}} -headerskip {{n}} {{path/to/image.raw}} > {{path/to/output.ppm}}`

- 忽略指定文件每行的最后 m 个字节：

`rawtoppm {{width}} {{height}} -rowskip {{m}} {{path/to/image.raw}} > {{path/to/output.ppm}}`

- 指定每个像素的颜色分量顺序：

`rawtoppm {{width}} {{height}} -{{rgb|rbg|grb|gbr|brg|bgr}} {{path/to/image.raw}} > {{path/to/output.ppm}}`
