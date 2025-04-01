# pbmreduce

> 按比例减小 PBM 图像。
> 参见：`pamenlarge`，`pamditherbw`。
> 更多信息：<https://netpbm.sourceforge.net/doc/pbmreduce.html>。

- 按指定的因子减小指定的图像：

`pbmreduce {{n}} {{path/to/image.pbm}} > {{path/to/output.pbm}}`

- 在减小时使用简单阈值：

`pbmreduce -threshold {{n}} {{path/to/image.pbm}} > {{path/to/output.pbm}}`

- 对所有量化使用指定的阈值：

`pbmreduce -value {{0.6}} {{n}} {{path/to/image.pbm}} > {{path/to/output.pbm}}`
