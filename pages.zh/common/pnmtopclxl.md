# pnmtopclxl

> 将 PNM 文件转换为 HP LaserJet PCL XL 打印机数据流。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmtopclxl.html>。

- 将 PNM 文件转换为 HP LaserJet PCL XL 打印机数据流：

`pnmtopclxl {{path/to/input1.pnm path/to/input2.pnm ...}} > {{path/to/output.pclxl}}`

- 指定图像的分辨率以及每张图像从左上角开始的位置偏移：

`pnmtopclxl -dpi {{resolution}} -xoffs {{x_offset}} -yoffs {{y_offset}} {{path/to/input1.pnm path/to/input2.pnm ...}} > {{path/to/output.pclxl}}`

- 为指定的纸张格式生成双面打印数据流：

`pnmtopclxl -duplex {{vertical|horizontal}} -format {{letter|legal|a3|a4|a5|...}} {{path/to/input1.pnm path/to/input2.pnm ...}} > {{path/to/output.pclxl}}`