# pstopnm

> 将 PostScript 文件转换为 PNM 图像。
> 更多信息：<https://netpbm.sourceforge.net/doc/pstopnm.html>。

- 将 PS 文件转换为 PNM 图像，将输入文件的第 N 页保存为 `path/to/fileN.ppm`：

`pstopnm {{path/to/file.ps}}`

- 明确指定输出格式：

`pstopnm -{{pbm|pgm|ppm}} {{path/to/file.ps}}`

- 指定输出的分辨率（每英寸点数）：

`pstopnm -dpi {{n}} {{path/to/file.ps}}`
