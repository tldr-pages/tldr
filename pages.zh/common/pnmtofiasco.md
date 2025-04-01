# pnmtofiasco

> 将 PNM 图像转换为压缩的 FIASCO 文件。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmtofiasco.html>.

- 将 PNM 图像转换为压缩的 FIASCO 文件：

`pnmtofiasco {{path/to/file.pnm}} > {{path/to/file.fiasco}}`

- 通过模式指定输入文件：

`pnmtofiasco {{[-i|--image-name]}} "{{img[01-09+1].pnm}}" > {{path/to/file.fiasco}}`

- 指定压缩质量：

`pnmtofiasco {{[-q|--quality]}} {{quality_level}} {{path/to/file.pnm}} > {{path/to/file.fiasco}}`

- 从指定的配置文件中加载要使用的选项：

`pnmtofiasco {{[-f|--config]}} {{path/to/fiascorc}} {{path/to/file.pnm}} > {{path/to/file.fiasco}}`
