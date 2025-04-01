# tifftopnm

> 将 TIFF 图像转换为 PNM 图像。
> 更多信息： <https://netpbm.sourceforge.net/doc/tifftopnm.html>.

- 将 TIFF 转换为 PNM 文件：

`tifftopnm {{path/to/input_file.tiff}} > {{path/to/output_file.pnm}}`

- 创建一个包含输入图像 alpha 通道的 PGM 文件：

`tifftopnm -alphaout {{path/to/alpha_file.pgm}} {{path/to/input_file.tiff}} > {{path/to/output_file.pnm}}`

- 遵循输入 TIFF 图像中的 `fillorder` 标签：

`tifftopnm -respectfillorder {{path/to/input_file.tiff}} > {{path/to/output_file.pnm}}`

- 将 TIFF 头信息打印到 `stderr`：

`tifftopnm -headerdump {{path/to/input_file.tiff}} > {{path/to/output_file.pnm}}`
