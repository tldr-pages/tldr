# avifenc

> AV1 图像文件格式 (AVIF) 编码器。
> 更多信息：<https://aomediacodec.github.io/av1-avif/>.

- 将特定的 PNG 图像转换为 AVIF：

`avifenc {{path/to/input.png}} {{path/to/output.avif}}`

- 使用特定的速度进行编码（6 为默认值，0 最慢，10 最快）：

`avifenc --speed {{2}} {{path/to/input.png}} {{path/to/output.avif}}`
