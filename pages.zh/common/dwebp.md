# dwebp

> `dwebp` 将 WebP 文件解压缩为 PNG、PAM、PPM 或 PGM 图像。
> 不支持动画 WebP 文件。
> 更多信息请访问：<https://developers.google.com/speed/webp/docs/dwebp/>。

- 将 WebP 文件转换为 PNG 文件：

`dwebp {{path/to/input.webp}} -o {{path/to/output.png}}`

- 将 WebP 文件转换为特定文件类型：

`dwebp {{path/to/input.webp}} -bmp|-tiff|-pam|-ppm|-pgm|-yuv -o {{path/to/output}}`

- 转换 WebP 文件，尽可能使用多线程：

`dwebp {{path/to/input.webp}} -o {{path/to/output.png}} -mt`

- 转换 WebP 文件，同时裁剪和缩放：

`dwebp {{input.webp}} -o {{output.png}} -crop {{x_pos}} {{y_pos}} {{width}} {{height}} -scale {{width}} {{height}}`

- 转换 WebP 文件并翻转输出：

`dwebp {{path/to/input.webp}} -o {{path/to/output.png}} -flip`

- 转换 WebP 文件，并不使用循环滤波以加快解码过程：

`dwebp {{path/to/input.webp}} -o {{path/to/output.png}} -nofilter`