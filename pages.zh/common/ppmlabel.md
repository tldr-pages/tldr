# ppmlabel

> 向 PPM 图像添加文本。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmlabel.html>.

- 向 PPM 图像的指定位置添加文本：

`ppmlabel -x {{pos_x}} -y {{pos_y}} -text {{text}} {{path/to/input_file.ppm}} > {{path/to/output_file.ppm}}`

- 在不同位置添加多个文本：

`ppmlabel -x {{pos_x1}} -y {{pos_y1}} -text {{text1}} -x {{pos_x2}} -y {{pos_y2}} -text {{text2}} {{path/to/input_file.ppm}} > {{path/to/output_file.ppm}}`

- 指定添加文本的线条颜色、背景颜色、倾斜角度和大小：

`ppmlabel -x {{pos_x}} -y {{pos_y}} -color {{line_color}} -background {{background_color}} -angle {{tilt}} -size {{size}} -text {{text}} {{path/to/input_file.ppm}} > {{path/to/output_file.ppm}}`