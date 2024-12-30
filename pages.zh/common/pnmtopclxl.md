# pnmtopclxl

> 将PNM文件转换为HP LaserJet PCL XL打印机流。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmtopclxl.html>。

- 将PNM文件转换为HP LaserJet PCL XL打印机流：

`pnmtopclxl {{path/to/input1.pnm path/to/input2.pnm ...}} > {{path/to/output.pclxl}}`

- 指定图像的分辨率以及每张图像的左上角位置：

`pnmtopclxl -dpi {{resolution}} -xoffs {{x_offset}} -yoffs {{y_offset}} {{path/to/input1.pnm path/to/input2.pnm ...}} > {{path/to/output.pclxl}}`

- 为指定纸张格式生成双面打印机流：

`pnmtopclxl -duplex {{vertical|horizontal}} -format {{letter|legal|a3|a4|a5|...}} {{path/to/input1.pnm path/to/input2.pnm ...}} > {{path/to/output.pclxl}}`