# rawtopgm

> 将一个原始灰度图像转换为 PGM 图像。
> 更多信息：<https://netpbm.sourceforge.net/doc/rawtopgm.html>。

- 将一个原始灰度图像转换为 PGM 图像：

`rawtopgm {{宽度}} {{高度}} {{path/to/image.raw}} > {{path/to/output.pgm}}`

- 将一个原始灰度图像转换为 PGM 图像，假设图像是正方形：

`rawtopgm {{path/to/image.raw}} > {{path/to/output.pgm}}`

- 将一个像素顺序为从底部开始而非顶部开始的原始灰度图像转换为 PGM 图像：

`rawtopgm {{宽度}} {{高度}} -bottomfirst {{path/to/image.raw}} > {{path/to/output.pgm}}`

- 忽略指定文件的前 `n` 个字节：

`rawtopgm {{宽度}} {{高度}} -headerskip {{n}} {{path/to/image.raw}} > {{path/to/output.pgm}}`

- 忽略指定文件中每行的最后 `m` 个字节：

`rawtopgm {{宽度}} {{高度}} -rowskip {{m}} {{path/to/image.raw}} > {{path/to/output.pgm}}`

- 指定输入灰度值的最大值为 `n`：

`rawtopgm {{宽度}} {{高度}} -maxval {{n}} {{path/to/image.raw}} > {{path/to/output.pgm}}`

- 指定表示输入中每个样本的字节数，并且字节序为小端模式：

`rawtopgm {{宽度}} {{高度}} -bpp {{1|2}} -littleendian {{path/to/image.raw}} > {{path/to/output.pgm}}`