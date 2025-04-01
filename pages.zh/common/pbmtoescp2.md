# pbmtoescp2

> 将 PBM 图像转换为 ESC/P2 打印机文件。
> 另见：`pbmtoepson`, `escp2topbm`。
> 更多信息：<https://netpbm.sourceforge.net/doc/pbmtoescp2.html>。

- 将 PBM 图像转换为 ESC/P2 打印机文件：

`pbmtoescp2 {{path/to/image.pbm}} > {{path/to/output.escp2}}`

- 指定输出的压缩方式：

`pbmtoescp2 -compression {{0|1}} {{path/to/image.pbm}} > {{path/to/output.escp2}}`

- 指定输出的水平和垂直分辨率（每英寸点数）：

`pbmtoescp2 -resolution {{180|360|720}} {{path/to/image.pbm}} > {{path/to/output.escp2}}`

- 在输出的末尾添加换页命令：

`pbmtoescp2 -formfeed {{path/to/image.pbm}} > {{path/to/output.escp2}}`