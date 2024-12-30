# ppmtopjxl

> 将 PPM 图像转换为 HP PaintJet XL PCL 文件。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmtopjxl.html>。

- 将 PPM 图像转换为 PJXL 文件：

`ppmtopjxl {{path/to/image.ppm}} > {{path/to/output.pjxl}}`

- 调整输入图像的大小：

`ppmtopjxl -xsize {{10cm}} -ysize {{5cm}} {{path/to/image.ppm}} > {{path/to/output.pjxl}}`

- 移动输入图像：

`ppmtopjxl -xshift {{10pt}} -yshift {{5pt}} {{path/to/image.ppm}} > {{path/to/output.pjxl}}`

- 不使用常规的 TIFF 4.0 压缩方法：

`ppmtopjxl -nopack {{path/to/image.ppm}} > {{path/to/output.pjxl}}`