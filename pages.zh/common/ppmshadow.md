# ppmshadow

> 为 PPM 图像添加模拟阴影。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmshadow.html>.

- 为 PPM 图像添加模拟阴影：

`ppmshadow {{path/to/input_file.ppm}} > {{path/to/output_file.ppm}}`

- 通过指定的像素数来[模糊]图像：

`ppmshadow -b {{n}} {{path/to/input_file.ppm}} > {{path/to/output_file.ppm}}`

- 指定模拟光源相对于图像左边缘和顶部的位移：

`ppmshadow -x {{left_offset}} -y {{top_offset}} {{path/to/input_file.ppm}} > {{path/to/output_file.ppm}}`