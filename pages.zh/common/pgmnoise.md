# pgmnoise

> 生成白噪声。
> 更多信息：<https://netpbm.sourceforge.net/doc/pgmnoise.html>。

- 生成包含白噪声的PGM图像：

`pgmnoise {{宽度}} {{高度}} > {{输出路径/输出.pgm}}`

- 指定伪随机数生成器的种子：

`pgmnoise {{宽度}} {{高度}} -randomseed {{值}} > {{输出路径/输出.pgm}}`