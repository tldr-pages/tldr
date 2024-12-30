# rletopnm

> 将犹他光栅工具的RLE图像文件转换为PNM文件。
> 更多信息：<https://netpbm.sourceforge.net/doc/rletopnm.html>。

- 将RLE图像转换为PNM文件：

`rletopnm {{path/to/input.rle}} > {{path/to/output.pnm}}`

- 创建包含RLE文件的alpha通道的PGM图像：

`rletopnm -alphaout {{path/to/alpha_file.pgm}} {{path/to/input.rle}} > {{path/to/output.pnm}}`

- 以详细模式操作并将RLE头的内容打印到`stdout`：

`rletopnm -verbose {{path/to/input.rle}} > {{path/to/output.pnm}}`