# pcxtoppm

> 将 PCX 文件转换为 PPM 图像。
> 更多信息：<https://netpbm.sourceforge.net/doc/pcxtoppm.html>.

- 将 PCX 文件转换为 PPM 图像：

`pcxtoppm {{path/to/file.pcx}} > {{path/to/file.ppm}}`

- 即使 PCX 文件提供了调色板，也使用预定义的标准调色板：

`pcxtoppm -stdpalette {{path/to/file.pcx}} > {{path/to/file.ppm}}`

- 将 PCX 头信息打印到 `stdout`：

`pcxtoppm -verbose {{path/to/file.pcx}} > {{path/to/file.ppm}}`
