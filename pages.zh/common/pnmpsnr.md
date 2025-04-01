# pnmpsnr

> 计算两幅图像之间的差异。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmpsnr.html>.

- 计算两幅图像之间的差异，即峰值信号噪声比（PSNR）：

`pnmpsnr {{path/to/file1.pnm}} {{path/to/file2.pnm}}`

- 比较图像的色彩分量而不是亮度和色度分量：

`pnmpsnr {{path/to/file1.pnm}} {{path/to/file2.pnm}} -rgb`

- 以比较模式运行，即仅根据计算的 PSNR 是否超过 `n` 输出 `nomatch` 或 `match`：

`pnmpsnr {{path/to/file1.pnm}} {{path/to/file2.pnm}} -target {{n}}`

- 以比较模式运行并分别比较各个图像分量，即 Y、Cb 和 Cr，与相应的阈值：

`pnmpsnr {{path/to/file1.pnm}} {{path/to/file2.pnm}} -target1 {{threshold_Y}} -target2 {{threshold_Cb}} -target3 {{threshold_Cr}}`

- 以比较模式运行并分别比较各个图像分量，即红、绿和蓝，与相应的阈值：

`pnmpsnr {{path/to/file1.pnm}} {{path/to/file2.pnm}} -rgb -target1 {{threshold_red}} -target2 {{threshold_green}} -target3 {{threshold_blue}}`

- 生成可被机器解析的输出：

`pnmpsnr {{path/to/file1.pnm}} {{path/to/file2.pnm}} -machine`