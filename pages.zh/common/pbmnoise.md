# pbmnoise

> 生成白噪声图像。
> 更多信息：<https://netpbm.sourceforge.net/doc/pbmnoise.html>。

- 生成一个包含白噪声的 PGM 图像：

`pbmnoise {{width}} {{height}} > {{path/to/output.pbm}}`

- 指定伪随机数生成器的种子：

`pbmnoise {{width}} {{height}} -randomseed {{value}} > {{path/to/output.pbm}}`

- 指定白像素与黑像素的比例：

`pbmnoise {{width}} {{height}} -ratio {{1/3}} > {{path/to/output.pbm}}`