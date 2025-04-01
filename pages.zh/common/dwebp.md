# dwebp

> `dwebp` 将 WebP 文件解压缩为 PNG、PAM、PPM 或 PGM 图像。
> 不支持动画 WebP 文件。
> 更多信息：<https://developers.google.com/speed/webp/docs/dwebp>.

- 将 WebP 文件转换为 PNG 文件：

`dwebp {{path/to/input.webp}} -o {{path/to/output.png}}`

- 将 WebP 文件转换为指定的文件类型：

`dwebp {{path/to/input.webp}} -bmp|-tiff|-pam|-ppm|-pgm|-yuv -o {{path/to/output}}`

- 将 WebP 文件转换为 PNG 文件，如果可能则使用多线程：

`dwebp {{path/to/input.webp}} -o {{path/to/output.png}} -mt`

- 将 WebP 文件转换为 PNG 文件，同时裁剪和缩放：

`dwebp {{input.webp}} -o {{output.png}} -crop {{x_pos}} {{y_pos}} {{width}} {{height}} -scale {{width}} {{height}}`

- 将 WebP 文件转换为 PNG 文件并翻转输出：

`dwebp {{path/to/input.webp}} -o {{path/to/output.png}} -flip`

- 将 WebP 文件转换为 PNG 文件，不使用循环滤波以加快解码过程：

`dwebp {{path/to/input.webp}} -o {{path/to/output.png}} -nofilter`