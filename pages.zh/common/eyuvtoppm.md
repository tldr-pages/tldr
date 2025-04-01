# eyuvtoppm

> 将 Berkeley YUV 文件转换为 PPM 格式。
> 更多信息：<https://netpbm.sourceforge.net/doc/eyuvtoppm.html>.

- 从指定的输入文件读取 Berkeley YUV 文件，将其转换为 PPM 图像并存储在指定的输出文件中：

`eyuvtoppm --width {{width}} --height {{height}} {{path/to/input_file.eyuv}} > {{path/to/output_file.ppm}}`