# cjxl

> 将图像压缩为 JPEG XL 格式。
> 接受的输入扩展名包括 PNG, APNG, GIF, JPEG, EXR, PPM, PFM, PAM, PGX 和 JXL。
> 更多信息：<https://github.com/libjxl/libjxl>。

- 将图像转换为 JPEG XL 格式：

`cjxl {{path/to/image.ext}} {{path/to/output.jxl}}`

- 将质量设置为无损并对结果图像进行最大压缩：

`cjxl --distance 0 --effort 9 {{path/to/image.ext}} {{path/to/output.jxl}}`

- 显示极其详细的帮助页面：

`cjxl {{[-h -v -v -v -v|--help --verbose --verbose --verbose --verbose]}}`
