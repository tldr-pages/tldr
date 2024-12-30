# pgmhist

> 打印PGM图像中存在的值的直方图。
> 另见：`ppmhist`。
> 更多信息：<https://netpbm.sourceforge.net/doc/pgmhist.html>。

- 显示人类可读的直方图：

`pgmhist {{path/to/image.pgm}}`

- 显示中位灰度值：

`pgmhist -median {{path/to/image.pgm}}`

- 显示四分位灰度值：

`pgmhist -quartile {{path/to/image.pgm}}`

- 报告存在无效灰度值：

`pgmhist -forensic {{path/to/image.pgm}}`

- 显示机器可读的输出：

`pgmhist -machine {{path/to/image.pgm}}`