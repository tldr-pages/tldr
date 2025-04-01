# pbmmake

> 创建一个空白的位图。
> 更多信息：<https://netpbm.sourceforge.net/doc/pbmmake.html>。

- 创建指定尺寸的空白位图：

`pbmmake {{width}} {{height}} > {{path/to/output_file.pbm}}`

- 指定位图的颜色：

`pbmmake -{{white|black|grey}} {{width}} {{height}} > {{path/to/output_file.pbm}}`