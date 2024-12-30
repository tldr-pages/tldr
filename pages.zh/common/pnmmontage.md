# pnmmontage

> 从多个 PNM 图像创建拼贴。
> 更多信息: <https://netpbm.sourceforge.net/doc/pnmmontage.html>。

- 生成指定图像的拼贴：

`pnmmontage {{path/to/image1.pnm path/to/image2.pnm ...}} > {{path/to/output.pnm}}`

- 指定拼贴的质量（注意：更大的值会生成更小的拼贴，但计算时间更长。）：

`pnmmontage -{{0..9}} {{path/to/image1.pnm path/to/image2.pnm ...}} > {{path/to/output.pnm}}`

- 生成不大于 `p` 百分比的最优拼贴：

`pnmmontage -quality {{p}} {{path/to/image1.pnm path/to/image2.pnm ...}} > {{path/to/output.pnm}}`

- 将输入文件在拼贴图像中的位置写入机器可读的文件：

`pnmmontage -data {{path/to/datafile}} {{path/to/image1.pnm path/to/image2.pnm ...}} > {{path/to/output.pnm}}`