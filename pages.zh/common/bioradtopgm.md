# bioradtopgm

> 将 Biorad 共聚焦文件转换为 PGM 文件。
> 更多信息：<https://netpbm.sourceforge.net/doc/bioradtopgm.html>。

- 读取 Biorad 共聚焦文件，并将其中的第 n 幅图像存储为 PGM 文件：

`bioradtopgm -{{n}} {{path/to/file.pic}} > {{path/to/file.pgm}}`

- 读取 Biorad 共聚焦文件并打印其中包含的图像数量：

`bioradtopgm {{path/to/file.pic}}`

- 显示版本信息：

`bioradtopgm -version`
