# rletopnm

> 将 Utah Raster Tools RLE 图像文件转换为 PNM 文件。
> 更多信息：<https://netpbm.sourceforge.net/doc/rletopnm.html>.

- 将 RLE 图像转换为 PNM 文件：

`rletopnm {{path/to/input.rle}} > {{path/to/output.pnm}}`

- 创建包含 RLE 文件的 alpha 通道的 PGM 图像：

`rletopnm -alphaout {{path/to/alpha_file.pgm}} {{path/to/input.rle}} > {{path/to/output.pnm}}`

- 以详细模式运行，并将 RLE 头的内容打印到 `stdout`：

`rletopnm -verbose {{path/to/input.rle}} > {{path/to/output.pnm}}`