# pnmtotiffcmyk

> 将PNM图像转换为CMYK编码的TIFF。
> 详细信息：<https://netpbm.sourceforge.net/doc/pnmtotiffcmyk.html>。

- 将PNM图像转换为CMYK编码的TIFF：

`pnmtotiffcmyk {{path/to/input_file.pnm}} > {{path/to/output_file.tiff}}`

- 指定TIFF压缩方法：

`pnmtotiffcmyk -{{none|packbits|lzw}} {{path/to/input_file.pnm}} > {{path/to/output_file.tiff}}`

- 控制填充顺序：

`pnmtotiffcmyk -{{msb2lsb|lsb2msb}} {{path/to/input_file.pnm}} > {{path/to/output_file.tiff}}`