# ppmspread

> 通过随机化的方式位移 PPM 图像中的像素。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmspread.html>。

- 以随机的方式位移 PPM 图像中的像素，位移量最大为：

`ppmspread {{a}} {{path/to/input_file.ppm}} > {{path/to/output_file.ppm}}`

- 指定伪随机数生成器的种子：

`ppmspread {{a}} {{path/to/input_file.ppm}} -randomseed {{seed}} > {{path/to/output_file.ppm}}`