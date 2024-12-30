# pbmnoise

> 生成白噪音。
> 更多信息：<https://netpbm.sourceforge.net/doc/pbmnoise.html>。

- 生成包含白噪音的PGM图像：

`pbmnoise {{宽度}} {{高度}} > {{输出路径/输出.pbm}}`

- 指定伪随机数生成器的种子：

`pbmnoise {{宽度}} {{高度}} -randomseed {{值}} > {{输出路径/输出.pbm}}`

- 指定白色像素与黑色像素的期望比例：

`pbmnoise {{宽度}} {{高度}} -ratio {{1/3}} > {{输出路径/输出.pbm}}`