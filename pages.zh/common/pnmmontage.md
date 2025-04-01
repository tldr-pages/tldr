# pnmmontage

> 从多个 PNM 图像创建一个拼贴图。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmmontage.html>.

- 从指定的图像生成拼贴图：

`pnmmontage {{path/to/image1.pnm path/to/image2.pnm ...}} > {{path/to/output.pnm}}`

- 指定拼贴图的质量（注意：较大的值会产生更小的拼贴图，但计算时间更长）：

`pnmmontage -{{0..9}} {{path/to/image1.pnm path/to/image2.pnm ...}} > {{path/to/output.pnm}}`

- 生成的拼贴图大小不超过最优拼贴图的 `p` 百分比：

`pnmmontage -quality {{p}} {{path/to/image1.pnm path/to/image2.pnm ...}} > {{path/to/output.pnm}}`

- 将输入文件在拼贴图中的位置写入一个机器可读文件：

`pnmmontage -data {{path/to/datafile}} {{path/to/image1.pnm path/to/image2.pnm ...}} > {{path/to/output.pnm}}`
