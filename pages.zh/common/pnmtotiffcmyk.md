# pnmtotiffcmyk

> 将 PNM 图像转换为 CMYK 编码的 TIFF。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmtotiffcmyk.html>。

- 将 PNM 图像转换为 CMYK 编码的 TIFF：

`pnmtotiffcmyk {{path/to/input_file.pnm}} > {{path/to/output_file.tiff}}`

- 指定 TIFF 压缩方法：

`pnmtotiffcmyk -{{none|packbits|lzw}} {{path/to/input_file.pnm}} > {{path/to/output_file.tiff}}`

- 控制填充顺序：

`pnmtotiffcmyk -{{msb2lsb|lsb2msb}} {{path/to/input_file.pnm}} > {{path/to/output_file.tiff}}`