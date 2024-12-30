# pbmreduce

> 按比例缩小PBM图像。
> 另见：`pamenlarge`，`pamditherbw`。
> 更多信息：<https://netpbm.sourceforge.net/doc/pbmreduce.html>。

- 按指定因子缩小指定图像：

`pbmreduce {{N}} {{path/to/image.pbm}} > {{path/to/output.pbm}}`

- 在缩小时使用简单的阈值处理：

`pbmreduce -threshold {{N}} {{path/to/image.pbm}} > {{path/to/output.pbm}}`

- 对所有量化使用指定的阈值：

`pbmreduce -value {{0.6}} {{N}} {{path/to/image.pbm}} > {{path/to/output.pbm}}`