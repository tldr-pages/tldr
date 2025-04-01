# tgatoppm

> 将 TrueVision Targa 文件转换为 Netpbm 图像。
> 更多信息：<https://netpbm.sourceforge.net/doc/tgatoppm.html>。

- 将 TrueVision Targa 文件转换为 PPM 图像：

`tgatoppm {{path/to/file.tga}} > {{path/to/output.ppm}}`

- 将 TGA 文件头中的信息输出到 `stdout`：

`tgatoppm --headerdump {{path/to/file.tga}}`

- 将输入图像的透明通道值写入指定文件：

`tgatoppm --alphaout {{path/to/transparency_file.pgm}} {{path/to/file.tga}} > {{path/to/output.ppm}}`

- 显示版本：

`tgatoppm -version`
