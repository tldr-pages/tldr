# rawtopgm

> 将原始灰度图像转换为PGM图像。
> 更多信息：<https://netpbm.sourceforge.net/doc/rawtopgm.html>。

- 将原始灰度图像转换为PGM图像：

`rawtopgm {{宽度}} {{高度}} {{路径/到/图像.raw}} > {{路径/到/输出.pgm}}`

- 将原始灰度图像转换为PGM图像，假设图像为正方形：

`rawtopgm {{路径/到/图像.raw}} > {{路径/到/输出.pgm}}`

- 将原始灰度图像（像素从底部开始而不是从顶部开始）转换为PGM图像：

`rawtopgm {{宽度}} {{高度}} -bottomfirst {{路径/到/图像.raw}} > {{路径/到/输出.pgm}}`

- 忽略指定文件的前n个字节：

`rawtopgm {{宽度}} {{高度}} -headerskip {{n}} {{路径/到/图像.raw}} > {{路径/到/输出.pgm}}`

- 忽略指定文件中每行的最后m个字节：

`rawtopgm {{宽度}} {{高度}} -rowskip {{m}} {{路径/到/图像.raw}} > {{路径/到/输出.pgm}}`

- 指定输入中灰度值的最大值等于N：

`rawtopgm {{宽度}} {{高度}} -maxval {{N}} {{路径/到/图像.raw}} > {{路径/到/输出.pgm}}`

- 指定输入中每个样本所占的字节数，并且字节序列应被解释为小端：

`rawtopgm {{宽度}} {{高度}} -bpp {{1|2}} -littleendian {{路径/到/图像.raw}} > {{路径/到/输出.pgm}}`