# bioradtopgm

> 将Biorad共聚焦文件转换为PGM文件。
> 更多信息：<https://netpbm.sourceforge.net/doc/bioradtopgm.html>。

- 读取Biorad共聚焦文件并将其中的第n幅图像存储为PGM文件：

`bioradtopgm -{{n}} {{path/to/file.pic}} > {{path/to/file.pgm}}`

- 读取Biorad共聚焦文件并打印它包含的图像数量：

`bioradtopgm {{path/to/file.pic}}`

- 显示版本信息：

`bioradtopgm -version`