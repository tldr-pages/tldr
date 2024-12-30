# pamtotiff

> 将 PAM 图像转换为 TIFF 文件。
> 更多信息：<https://netpbm.sourceforge.net/doc/pamtotiff.html>。

- 将 PAM 图像转换为 TIFF 图像：

`pamtotiff {{path/to/input_file.pam}} > {{path/to/output_file.tiff}}`

- 显式指定输出文件的压缩方法：

`pamtotiff -{{none|packbits|lzw|g3|g4|flate|adobeflate}} {{path/to/input_file.pam}} > {{path/to/output_file.tiff}}`

- 始终生成彩色 TIFF 图像，即使输入图像是灰度：

`pamtotiff -color {{path/to/input_file.pam}} > {{path/to/output_file.tiff}}`