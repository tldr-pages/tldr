# cjxl

> 将图像压缩为 JPEG XL。
> 接受的输入扩展名包括 PNG、APNG、GIF、JPEG、EXR、PPM、PFM、PAM、PGX 和 JXL。
> 更多信息：<https://github.com/libjxl/libjxl>。

- 将图像转换为 JPEG XL：

`cjxl {{路径/到/图像.ext}} {{路径/到/输出.jxl}}`

- 将质量设置为无损，并最大化生成图像的压缩：

`cjxl --distance 0 --effort 9 {{路径/到/图像.ext}} {{路径/到/输出.jxl}}`

- 显示极其详细的帮助页面：

`cjxl --help --verbose --verbose --verbose --verbose`