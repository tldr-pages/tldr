# pbmtoepson

> 将 PBM 图像转换为 Epson 打印机图形。
> 另请参阅：`pbmtoescp2`。
> 更多信息：<https://netpbm.sourceforge.net/doc/pbmtoepson.html>。

- 将 PBM 图像转换为 Epson 打印机图形：

`pbmtoepson {{path/to/image.pbm}} > {{path/to/output.epson}}`

- 指定输出的打印机协议：

`pbmtoepson -protocol {{escp9|escp}} {{path/to/image.pbm}} > {{path/to/output.epson}}`

- 指定输出的水平 DPI：

`pbmtoepson -dpi {{60|72|80|90|120|144|240}} {{path/to/image.pbm}} > {{path/to/output.epson}}`