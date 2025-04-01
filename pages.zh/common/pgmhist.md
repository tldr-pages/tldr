# pgmhist

> 打印 PGM 图像中出现的值的直方图。
> 参见: `ppmhist`。
> 更多信息: <https://netpbm.sourceforge.net/doc/pgmhist.html>。

- 以人类可读的方式显示直方图：

`pgmhist {{path/to/image.pgm}}`

- 显示中值灰度值：

`pgmhist -median {{path/to/image.pgm}}`

- 显示四个四分位数的灰度值：

`pgmhist -quartile {{path/to/image.pgm}}`

- 报告无效灰度值的存在：

`pgmhist -forensic {{path/to/image.pgm}}`

- 显示机器可读的输出：

`pgmhist -machine {{path/to/image.pgm}}`
