# ppmtobmp

> 将 PPM 图像转换为 BMP 文件。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmtobmp.html>。

- 将 PPM 图像转换为 BMP 文件：

`ppmtobmp {{path/to/file.ppm}} > {{path/to/file.bmp}}`

- 明确指定创建 Windows BMP 文件或 OS/2 BMP 文件：

`ppmtobmp -{{windows|os2}} {{path/to/file.ppm}} > {{path/to/file.bmp}}`

- 使用每个像素特定的位数：

`ppmtobmp -bbp {{1|4|8|24}} {{path/to/file.ppm}} > {{path/to/file.bmp}}`
