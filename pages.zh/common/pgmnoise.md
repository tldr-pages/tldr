# pgmnoise

> 生成白噪声。
> 更多信息：<https://netpbm.sourceforge.net/doc/pgmnoise.html>.

- 生成包含白噪声的 PGM 图像：

`pgmnoise {{width}} {{height}} > {{path/to/output.pgm}}`

- 指定伪随机数生成器的种子：

`pgmnoise {{width}} {{height}} -randomseed {{value}} > {{path/to/output.pgm}}`
