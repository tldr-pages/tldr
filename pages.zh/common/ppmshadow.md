# ppmshadow

> 向 PPM 图像添加模拟阴影。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmshadow.html>。

- 向 PPM 图像添加模拟阴影：

`ppmshadow {{path/to/input_file.ppm}} > {{path/to/output_file.ppm}}`

- [b] 按指定像素数模糊图像：

`ppmshadow -b {{n}} {{path/to/input_file.ppm}} > {{path/to/output_file.ppm}}`

- 指定模拟光源在图像左侧和顶部的位移：

`ppmshadow -x {{left_offset}} -y {{top_offset}} {{path/to/input_file.ppm}} > {{path/to/output_file.ppm}}`