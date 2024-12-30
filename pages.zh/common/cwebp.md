# cwebp

> 将图像文件压缩为 WebP 文件。
> 更多信息：<https://developers.google.com/speed/webp/docs/cwebp>。

- 使用默认设置（q = 75）压缩 WebP 文件到 [o]utput 文件：

`cwebp {{path/to/image_file}} -o {{path/to/output.webp}}`

- 以最佳 [q]uality 和最大文件大小压缩 WebP 文件：

`cwebp {{path/to/image_file}} -o {{path/to/output.webp}} -q {{100}}`

- 以最差 [q]uality 和最小文件大小压缩 WebP 文件：

`cwebp {{path/to/image_file}} -o {{path/to/output.webp}} -q {{0}}`

- 压缩 WebP 文件并调整图像大小：

`cwebp {{path/to/image_file}} -o {{path/to/output.webp}} -resize {{width}} {{height}}`

- 压缩 WebP 文件并去除 alpha 通道信息：

`cwebp {{path/to/image_file}} -o {{path/to/output.webp}} -noalpha`