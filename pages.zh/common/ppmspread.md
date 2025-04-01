# ppmspread

> 将 PPM 图像中的像素随机位移指定的最大值。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmspread.html>.

- 将 PPM 图像中的像素随机位移最多 a 个单位：

`ppmspread {{a}} {{path/to/input_file.ppm}} > {{path/to/output_file.ppm}}`

- 指定一个伪随机数生成器的种子：

`ppmspread {{a}} {{path/to/input_file.ppm}} -randomseed {{seed}} > {{path/to/output_file.ppm}}`