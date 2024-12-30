# rawtoppm

> 将原始RGB流转换为PPM图像。
> 更多信息：<https://netpbm.sourceforge.net/doc/rawtoppm.html>。

- 将原始RGB流转换为PPM图像：

`rawtoppm {{宽度}} {{高度}} {{路径/到/图像.raw}} > {{路径/到/输出.ppm}}`

- 将像素从底部开始而不是从顶部开始的原始RGB流转换为PPM图像：

`rawtoppm {{宽度}} {{高度}} {{路径/到/图像.raw}} | pamflip -tb > {{路径/到/输出.ppm}}`

- 忽略指定文件的前n个字节：

`rawtoppm {{宽度}} {{高度}} -headerskip {{n}} {{路径/到/图像.raw}} > {{路径/到/输出.ppm}}`

- 忽略指定文件中每行的最后m个字节：

`rawtoppm {{宽度}} {{高度}} -rowskip {{m}} {{路径/到/图像.raw}} > {{路径/到/输出.ppm}}`

- 指定每个像素的颜色分量顺序：

`rawtoppm {{宽度}} {{高度}} -{{rgb|rbg|grb|gbr|brg|bgr}} {{路径/到/图像.raw}} > {{路径/到/输出.ppm}}`